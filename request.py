import requests
import json

TOKEN = ''
PREFIX = ['LEETCODE', 'GENERATOR', 'HEXNUMBER', 'TRIANGLE', 'ITERATOR', 'REQUESTS']
GROUP = ['1021', '1022']
ACTION = ['Added', 'Fixed', 'Refactored', 'Deleted', 'Moved']


def get_headers():
    return {'Authorization': 'token ' + TOKEN}


def get_all_pullrequests(owner, rep, state):
    pulls = requests.get('https://api.github.com/repos/{}/{}/pulls?state={}'.format(owner, rep, state),
                         headers=get_headers()).json()
    return pulls


def get_all_commits(pullrequest):
    messages = []
    commits = requests.get(pullrequest['commits_url'], headers=get_headers()).json()
    for commit in commits:
        messages.append(commit['commit']['message'])
    return messages


def commit_verification(title):
    errors = []
    parts = title.split(' ')
    if len(parts) > 1:
        ident = parts[0].split('-')
        if len(ident) > 1:
            if not ident[0] in PREFIX:
                errors.append('Prefix should be one of the: {}'.format(', '.join(PREFIX)))
            if not ident[1] in GROUP:
                errors.append('Group should be one of the: {}'.format(', '.join(GROUP)))
            if not parts[1] in ACTION:
                errors.append('Action should be one of the: {}'.format(', '.join(ACTION)))
        else:
            errors.append('Prefix and group should be separated by hyphen.')
    else:
        errors.append('There should be prefix, group and action.')
    return '\n'.join(errors)


def send_error_message(pullrequest):
    errors = []
    errors.append(commit_verification(pullrequest['title']))
    for message in get_all_commits(pullrequest):
        result = commit_verification(message)
        if len(result) > 0:
            errors.append("'{}' is wrong:".format(message))
            errors.append(result)
    body = {'body': '\n'.join(errors)}
    cut = len(str(pullrequest['number'])) + 6  # отрезать от ссылки лишнее (pulls/number)
    pr = (pullrequest['url'])[:-cut]
    response = requests.post(pr + 'issues/' + str(pullrequest['number']) + '/comments', headers=get_headers(),
                             data=json.dumps(body))


def main():
    # file=open('user.txt')
    # lines=file.getlines()
    # owner,rep,state=lines[0],lines[1],lines[2]
    # file.close()
    owner, rep, state = 'croosky', 'python_au', 'all'
    pull_requests = get_all_pullrequests(owner, rep, state)
    for pull_request in pull_requests:
        send_error_message(pull_request)


if __name__ == '__main__':
    main()