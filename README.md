## Overview
This repo is a barebones Hugo website setup with GitHub Actions. On every push to `master`, the workflow `deploy.yml` will build `master` and push `/public` to `gh-pages`. The setup here is the final outcome of this blog post:
https://www.charlesjlee.com/post/20200517-github-actions/

## Required changes
If you fork this repo, there are three changes you need to make:
1. Create a deploy key named `ACTIONS_DEPLOY_KEY`. Steps available [here](https://www.charlesjlee.com/post/20200517-github-actions/#3-use-github-actions-to-deploy). This deploy key is used in `.github/workflows/deploy.yml`
2. In `.github/workflows/deploy.yml`, update `external_repository` to your username and repo
3. In `.github/workflows/deploy.yml`, update `user_name` and `user_email`

The `ananke` theme in `/themes` is a Git submodule and so will be empty if you clone this repo. This will lead to errors when developing locally. To pull the theme files, you can run `git submodule update --init --recursive`