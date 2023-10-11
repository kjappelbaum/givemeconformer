# -*- coding: utf-8 -*-

"""Main code."""

from pathlib import Path
from typing import Union

from rdkit.Chem import AllChem as Chem


def getRMS(mol, c1, c2):
    rms = Chem.GetBestRMS(mol, mol, c1, c2)
    return rms


def write_confs(mol, confs, outname, format: str = "sdf"):
    # add the format extension if not present
    if not outname.endswith(format):
        outname += "." + format
    if format == "sdf":
        with open(outname, "w") as f:
            w = Chem.SDWriter(f)
            for conf in confs.values():
                w.write(mol, conf)
            w.close()
    elif format == "mol":
        w = Chem.MolToMolFile(mol, outname)
    elif format == "xyz":
        w = Chem.MolToXYZFile(mol, outname)
    else:
        raise Exception("Format not recognized")


def optimize(mol, confid, ff: str = "uff"):
    if ff == "mmff":
        _converged = Chem.MMFFOptimizeMolecule(mol, confId=confid, maxIters=1000)
        return Chem.MMFFGetMoleculeForceField(
            mol, Chem.MMFFGetMoleculeProperties(mol), confId=confid
        ).CalcEnergy()
    elif ff == "uff":
        _converged = not Chem.UFFOptimizeMolecule(mol, confId=confid)
        return Chem.UFFGetMoleculeForceField(mol, confId=confid).CalcEnergy()


def _get_conformer(
    smiles: str,
    use_etkdg: bool = False,
    max_conformers: int = 1,
    num_samples: int = 1000,
    seed: int = 42,
    ff: str = "mmff",
    rms_threshold: float = 0.7,
    energy_window: float = 10,
):
    mol = Chem.MolFromSmiles(smiles)

    Chem.SanitizeMol(mol)
    mol = Chem.AddHs(mol)

    if use_etkdg:
        cids = Chem.EmbedMultipleConfs(mol, num_samples * max_conformers, Chem.ETKDG())
    else:
        cids = Chem.EmbedMultipleConfs(mol, num_samples * max_conformers, randomSeed=seed)

    energies = []
    for conf in cids:
        energies.append(optimize(mol, conf, ff))

    sorted_by_energy = sorted(zip(cids, energies), key=lambda x: x[1])
    lowest_energy = sorted_by_energy[0][1]
    write = {}
    for cid, energy in sorted_by_energy:
        if len(write) >= max_conformers:
            break
        # check rmsd
        passed = True
        for written_conf in write.keys():
            rms = getRMS(mol, written_conf, cid)
            if (rms < rms_threshold) or (
                energy_window > 0 and energy - lowest_energy > energy_window
            ):
                passed = False
                break
        if passed:
            write[conf] = True
    return mol, write


def get_conformer(
    smiles: str,
    use_etkdg: bool = False,
    max_conformers: int = 1,
    num_samples: int = 1000,
    seed: int = 42,
    ff: str = "mmff",
    rms_threshold: float = 0.7,
    energy_window: float = 10,
):
    mol, write = _get_conformer(
        smiles=smiles,
        use_etkdg=use_etkdg,
        max_conformers=max_conformers,
        num_samples=num_samples,
        seed=seed,
        ff=ff,
        rms_threshold=rms_threshold,
        energy_window=energy_window,
    )

    conformers = [mol.GetConformer(confid) for confid in write.keys()]
    return conformers


def create_conformer(
    smiles: str,
    use_etkdg: bool = False,
    max_conformers: int = 1,
    num_samples: int = 1000,
    seed: int = 42,
    ff: str = "mmff",
    rms_threshold: float = 0.7,
    energy_window: float = 10,
    outname: Union[str, Path] = "conformers",
    outformat: str = "sdf",
) -> str:
    mol, write = _get_conformer(
        smiles=smiles,
        use_etkdg=use_etkdg,
        max_conformers=max_conformers,
        num_samples=num_samples,
        seed=seed,
        ff=ff,
        rms_threshold=rms_threshold,
        energy_window=energy_window,
    )
    write_confs(mol, write, outname, outformat)

    print(f"Created {len(write)} conformers")
