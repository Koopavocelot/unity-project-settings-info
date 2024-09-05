from unityparser import UnityDocument
import os


def run():
    project_settings_file_path = 'ProjectSettings/ProjectSettings.asset'
    unity_document = UnityDocument.load_yaml(project_settings_file_path)
    projectsettings_monobehaviour_document = unity_document.entry

    bundle_version = ""
    bundle_code = 0
    try:
        bundle_version = projectsettings_monobehaviour_document.bundleVersion
        bundle_code = projectsettings_monobehaviour_document.AndroidBundleVersionCode
    except AttributeError:
        print("Failed to find bundleVersion in ProjectSettings.asset")
        return

    print("bundle_version: " + str(bundle_version))
    print("bundle_code: " + str(bundle_code))

    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        print(f'bundle-version={bundle_version}', file=fh)

    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        print(f'bundle-code={bundle_code}', file=fh)

    return


run()
