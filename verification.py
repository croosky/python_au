import requests
import re

TOKEN = 'f20683ab9b4227c373f132806b08b432fcc750c6'


def get_headers():
    return {'Authorization': 'token ' + TOKEN}


repos = requests.get('https://api.github.com/users/croosky/repos', headers=get_headers()).json()


class Github_requests:
    def __init__(self, owner='croosky', rep='python_au', state='all'):
        self.owner = owner
        self.rep = rep
        self.state = state

    def get_all_pullrequests(self):
        pulls = requests.get(
            'https://api.github.com/repos/{}/{}/pulls?state={}'.format(self.owner, self.rep, self.state),
            headers=get_headers()).json()
        return pulls

    def get_all_commits(self, pullrequest):
        messages = []
        commits = requests.get(pullrequest['commits_url'], headers=get_headers()).json()
        for commit in commits:
            messages.append(commit['commit']['message'])
        return messages

    def commit_verification(self, message):
        errors = []
        if not (re.match(r'LEETCODE-102', message) or re.match(r'GENERATOR-102', message) or re.match(r'HEXNUMBER-102',
                                                                                                      message) or re.match(
                r'TRIANGLE-102', message) or re.match(r'VERIFICATION-102', message) or re.match(r'ITERATOR-102',
                                                                                                message)):
            errors.append(
                'Identificator should be LEETCODE/GENERATOR/HEXNUMBER/TRIANGLE/ITERATOR/VERIFICATION-1021/1022.')
        if not (re.search(r'Added', message) or re.search(r'Refactored', message) or re.search(r'Deleted',
                                                                                               message) or re.search(
                r'Fixed', message)):
            errors.append('State should be Added/Refactored/Deleted/Fixed.')
        return errors

    def error_message(self, pullrequest):
        # Отправить сообщение на гитхаб
        output = ''
        for message in self.get_all_commits(pullrequest):
            errors = self.commit_verification(message)
            if len(errors) > 0:
                output += "Commit '{}' is wrong. {}\n".format(message, ''.join(errors))
        body = {'body': output}
        response = requests.post(
            'https://api.github.com/repos/{}/{}/issues/{}/comments'.format(self.owner, self.rep, pullrequest['number']),
            headers=get_headers(), data=json.dumps(body))


def main():
    # file=open('user.txt')
    # lines=file.getlines()
    # owner,rep,state=lines[0],lines[1],lines[2]
    # file.close()
    owner, rep, state = 'croosky', 'python_au', 'all'
    request = Github_requests()
    pull_requests = request.get_all_pullrequests()
    for pull_request in pull_requests:
        # print(pull_requests)
        request.error_message(pull_request)


if __name__ == '__main__':
    main()