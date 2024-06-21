import git_filter_repo as fr

# Commit vaqtini 2024-06-21 08:21:00 +0500 ga o'zgartirish
def set_commit_date(commit, attr_dict):
    attr_dict['GIT_AUTHOR_DATE'] = '2024-06-21 08:21:00 +0500'
    attr_dict['GIT_COMMITTER_DATE'] = '2024-06-21 08:21:00 +0500'
    return attr_dict

# Repozitoriy tarixini qayta yozish
fr.RepoFilter(
    repo='.',
    force=True,
    commits_callback=set_commit_date
).run()