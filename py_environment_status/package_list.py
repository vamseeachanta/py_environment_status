import pkg_resources


def package_list():
  installed_packages = pkg_resources.working_set
  installed_packages_list = sorted(
      ["%s==%s" % (i.key, i.version) for i in installed_packages])
  print(installed_packages_list)


if __name__ == '__main__':
  package_list()
