from unityparser import UnityDocument


def run():
    project_settings_file_path = 'ProjectSettings/ProjectSettings.asset'
    unity_document = UnityDocument.load_yaml(project_settings_file_path)
    projectsettings_monobehaviour_document = unity_document.entry

    try:
        bundle_version = projectsettings_monobehaviour_document.bundleVersion
    except AttributeError:
        print("Failed to find bundleVersion in ProjectSettings.asset")
        return

    print("bundle_version: " + str(bundle_version))

    # see https://docs.github.com/en/actions/reference/workflow-commands-for-github-actions#setting-an-output-parameter
    print(f"::set-output name=bundle-version::{bundle_version}")

    return


run()
