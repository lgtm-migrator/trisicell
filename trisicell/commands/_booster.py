import os

import click

import trisicell as tsc


@click.command(short_help="Run Booster.")
@click.argument(
    "genotype_file",
    required=True,
    type=click.Path(
        exists=True, file_okay=True, dir_okay=False, readable=True, resolve_path=True
    ),
)
@click.argument(
    "alpha",
    required=True,
    type=float,
)
@click.argument(
    "beta",
    required=True,
    type=float,
)
@click.option(
    "--solver",
    "-s",
    default="scite",
    type=click.Choice(["scite", "phiscs", "scistree"]),
    show_default=True,
    help="Solver of the booster.",
)
@click.option(
    "--sample_on",
    "-so",
    default="muts",
    type=click.Choice(["muts", "cells"]),
    show_default=True,
    help="Sampling on `muts` or `cells`.",
)
@click.option(
    "--sample_size",
    "-ss",
    default=10,
    type=int,
    show_default=True,
    help="The size of samples i.e. the number of muts or cells.",
)
@click.option(
    "--n_samples",
    "-ns",
    default=10,
    type=int,
    show_default=True,
    help="The number of subsamples.",
)
@click.option(
    "--begin_sample",
    "-bs",
    default=0,
    type=int,
    show_default=True,
    help="ID of the start subsample name.",
)
@click.option(
    "--n_jobs",
    "-nj",
    default=0,
    type=int,
    show_default=True,
    help="Number of parallel jobs to do subsampleing.",
)
@click.option(
    "--time_out",
    "-to",
    default=120,
    type=int,
    show_default=True,
    help="""Timeout of solving allowance
    (if solver is SCITE this parameter is the number of iterations)""",
)
def booster(
    genotype_file,
    alpha,
    beta,
    solver,
    sample_on,
    sample_size,
    n_samples,
    begin_sample,
    n_jobs,
    time_out,
):
    """Divide and Conquer

    trisicell booster input.SC 0.001 0.1
    -s scistree -so cells -ss 3 -ns 10 -bs 0 -nj 5 -to 3600
    """

    dirbase = tsc.ul.dirbase(genotype_file)
    dirname, basename = tsc.ul.dir_base(genotype_file)

    tsc.settings.verbosity = "info"
    # tsc.settings.logfile = f'{dirbase}.booster.log'

    df_in = tsc.io.read(genotype_file)
    df_out = tsc.tl.solver.booster(
        df_in,
        alpha=alpha,
        beta=beta,
        solver=solver,
        sample_on=sample_on,
        sample_size=sample_size,
        n_samples=n_samples,
        begin_sample=begin_sample,
        n_jobs=n_jobs,
        time_out=time_out,
        save_inter=True,
        dir_inter=".",
        base_inter=basename,
    )
    # tsc.io.write(df_out, f'{dirbase}.booster.CFMatrix')

    return None