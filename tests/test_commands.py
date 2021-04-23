import os

import pytest
from _helpers import *
from click.testing import CliRunner

import trisicell as tsc
from trisicell.commands.trisicell import cli


class TestCommands:
    def test_scistree(self):
        runner = CliRunner()
        result = runner.invoke(
            cli,
            [
                "scistree",
                f"{tsc.ul.get_file('trisicell.datasets/test/test.tsv')}",
                "0.0000001",
                "0.1",
            ],
        )
        assert result.exit_code == 0

    def test_scite(self):
        runner = CliRunner()
        result = runner.invoke(
            cli,
            [
                "scite",
                f"{tsc.ul.get_file('trisicell.datasets/test/test.tsv')}",
                "0.0000001",
                "0.1",
                "-r 3",
                "-l 1000",
            ],
        )
        assert result.exit_code == 0

    def test_scite_experiment(self):
        runner = CliRunner()
        result = runner.invoke(
            cli,
            [
                "scite",
                f"{tsc.ul.get_file('trisicell.datasets/test/test.tsv')}",
                "0.0000001",
                "0.1",
                "-r 3",
                "-l 1000",
                "-e",
                "-h 0.005",
            ],
        )
        assert result.exit_code == 0

    def test_phiscsb(self):
        runner = CliRunner()
        result = runner.invoke(
            cli,
            [
                "phiscsb",
                f"{tsc.ul.get_file('trisicell.datasets/test/test.tsv')}",
                "0.0000001",
                "0.1",
            ],
        )
        assert result.exit_code == 0

    def test_consensus(self):
        runner = CliRunner()
        result = runner.invoke(
            cli,
            [
                "consensus",
                f"{tsc.ul.get_file('trisicell.datasets/test/consensus/biorxiv.fig3b.CFMatrix')}",
                f"{tsc.ul.get_file('trisicell.datasets/test/consensus/biorxiv.figs18a.CFMatrix')}",
                f"{tsc.ul.get_file('trisicell.datasets/test/consensus.CFMatrix')}",
            ],
        )
        assert result.exit_code == 0

    def test_cf2newick(self):
        runner = CliRunner()
        result = runner.invoke(
            cli,
            [
                "cf2newick",
                f"{tsc.ul.get_file('trisicell.datasets/test/test.scite.CFMatrix')}",
            ],
        )
        assert result.exit_code == 0

    @skip_graphviz
    def test_cf2tree(self):
        runner = CliRunner()
        result = runner.invoke(
            cli,
            [
                "cf2tree",
                f"{tsc.ul.get_file('trisicell.datasets/test/test.scite.CFMatrix')}",
            ],
        )
        assert result.exit_code == 0


@pytest.fixture(scope="session", autouse=True)
def cleanup(request):
    def remove_test_dir():
        tsc.ul.remove(tsc.ul.get_file("trisicell.datasets/test/test.scistree.CFMatrix"))
        tsc.ul.remove(tsc.ul.get_file("trisicell.datasets/test/test.scistree.log"))
        tsc.ul.remove(tsc.ul.get_file("trisicell.datasets/test/test.scite.CFMatrix"))
        tsc.ul.remove(tsc.ul.get_file("trisicell.datasets/test/test.scite.log"))
        tsc.ul.remove(tsc.ul.get_file("trisicell.datasets/test/test.phiscsb.CFMatrix"))
        tsc.ul.remove(tsc.ul.get_file("trisicell.datasets/test/test.phiscsb.log"))
        tsc.ul.remove(tsc.ul.get_file("trisicell.datasets/test/consensus.CFMatrix"))
        tsc.ul.remove(tsc.ul.get_file("trisicell.datasets/test/test.scite.info2"))
        tsc.ul.remove(tsc.ul.get_file("trisicell.datasets/test/test.scite.newick"))
        tsc.ul.remove(tsc.ul.get_file("trisicell.datasets/test/test.scite.png"))

    request.addfinalizer(remove_test_dir)
