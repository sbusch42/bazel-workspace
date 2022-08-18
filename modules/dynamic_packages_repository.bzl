def _dynamic_packages_repository_impl(ctx):
    ctx.execute(["python3", "{}/scripts/generator.py".format(ctx.attr.workspace)], quiet=False)
    ctx.file("WORKSPACE", 'workspace(name = "dynamic_packages_repository")')

dynamic_packages_repository_rule = repository_rule(
    implementation = _dynamic_packages_repository_impl,
    attrs = {
        "workspace": attr.string(
            mandatory = True,
        ),
    },
)

def dynamic_packages_repository(workspace):
    """ Generates a set of sample bazel packages in an external repository"""
    dynamic_packages_repository_rule(
        name = "dynamic_packages_repository",
        workspace = workspace,
    )
