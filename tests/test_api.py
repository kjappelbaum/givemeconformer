from rdkit.Chem import AllChem as Chem

from givemeconformer.api import create_conformer


def test_create_conformer(tmp_path):
    """Test :func:`givemeconformer.api.create_conformer`."""
    outname = tmp_path / "conformers.sdf"
    create_conformer("CC", outname=outname)
    assert outname.exists()
    assert outname.stat().st_size > 0
    mol = Chem.SDMolSupplier(str(outname))[0]
    assert mol.GetNumAtoms() == 2
