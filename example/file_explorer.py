import file_explorer

if __name__ == '__main__':
    files=file_explorer.list_files("/ESP")
    print(files)
    file_explorer.list()
    file_explorer.change_dir("/ESP")
    file_explorer.list()
    file_explorer.cwd()
    file_explorer.create_dir("/new")
    file_explorer.exit_dir()