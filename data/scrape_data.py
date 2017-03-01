import getpass
import json
import requests
import os
import sys

from bs4 import BeautifulSoup

cookie = None


def get_cookie():
    global cookie
    while cookie is None:
        name = input('username')
        pas = getpass.getpass()
        data = '{"username":"' + name + '", "password":"' + pas + '"}'
        req = requests.post("https://pcs.cs.cloud.vt.edu/api/login/", data=data)
        if 'auth_token' in req.cookies:
            cookie = req.cookies['auth_token']
        else:
            print("Invalid login")
    return cookie


def load_problem(folder, problem_id, letter):
    url = 'https://pcs.cs.cloud.vt.edu/api/problems/{}/'.format(problem_id)
    print("loading {}".format(url))
    req = requests.get('https://pcs.cs.cloud.vt.edu/api/problems/{}/'.format(problem_id))
    js = json.loads(req.text)
    if 'content' not in js:
        req = requests.get('https://pcs.cs.cloud.vt.edu/api/problems/{}/'.format(problem_id),
                           cookies={'auth_token': get_cookie()})
        js = json.loads(req.text)
    if 'content' not in js:
        print(req.text)
        print("Could not load problem {}".format(problem_id))
        return
    bs = BeautifulSoup(js['content'])
    i = 0
    python_file_path = os.path.join(folder, 'pr{}.py'.format(letter))

    def remove_last_nl(string):
        return string[:len(string) - 1] if string[len(string) - 1] == '\n' else string

    if not os.path.exists(python_file_path):
        with open(python_file_path, 'w+') as python_file:
            python_file.write("""\nif __name__ == '__main__':\n    print("unimplemented")""")
    for table in bs.find_all('table'):
        in_val, out = [str(i).replace('<pre>', '').replace('</pre>', '') for i in table('pre')]
        in_val = remove_last_nl(in_val)
        out = remove_last_nl(out)
        with open(os.path.join(folder, 'pr{}_in_{}'.format(letter, i)), 'w+') as in_file:
            in_file.write(in_val)
        with open(os.path.join(folder, 'pr{}_out_{}'.format(letter, i)), 'w+') as out_file:
            out_file.write(out)
        i += 1


def load_contest(folder, contest_number):
    if not os.path.exists(folder):
        os.mkdir(folder)
    req = requests.get('https://pcs.cs.cloud.vt.edu/api/contests/{}/'.format(contest_number))
    letter = ord('A')
    for problem in req.json()['problems']:
        load_problem(folder, problem['id'], chr(letter))
        letter += 1


if __name__ == '__main__':
    # if len(sys.argv) != 3:
    #    print('This can only be called with 2 arguments. Date, and contest number')
    #    exit(-1)
    req = requests.get(str(sys.argv[1]))
    count = 0
    indexOfInputData = []
    indexOfOutputData = []

    inputOutput = []
    outputOutput = []

    lines_of_req = req.text.split('\n')
    for line in lines_of_req:
        if 'file input-' in line:
            indexOfInputData.append(count)
        if 'file output-' in line:
            indexOfOutputData.append(count)
        count = count + 1

    for idx in indexOfInputData:
        inFile = ""
        for i in xrange(1, 100000000):
            s = lines_of_req[idx + 2 + i - 1]
            if "<pre>" in s:
                s = s[s.find("<pre>") + len("<pre>"):]
            if "</pre>" in s:
                s = s[:s.find("</pre>")]
                inFile += s
                break
            inFile += s + "\n"
        inputOutput.append(inFile)
    # print(inputOutput)
    for idx in indexOfOutputData:
        inFile = ""
        for i in xrange(1, 100000000):
            s = lines_of_req[idx + 2 + i - 1]
            if "<pre>" in s:
                s = s[s.find("<pre>") + len("<pre>"):]
            if "</pre>" in s:
                s = s[:s.find("</pre>")]
                inFile += s
                break
            inFile += s + "\n"
        outputOutput.append(inFile)
    # print("\n".join(outputOutput))
    both = zip(inputOutput, outputOutput)
    # print('\n\n\n\n\n\n'.join(['Input:\n' + inn + "\nOutput:\n" + out for inn,out in both]))
    samplecases = 2
    count = 1
    for inn, out in both:
        if "..." in inn + out:
            continue
        else:
            prefix = "secret/secret-"
            sub = samplecases
            if count < samplecases + 1:
                prefix = "sample/sample-"
                sub = 0
            with open(prefix + str(count - sub) + ".in", "w") as f:
                f.write(inn)
            with open(prefix + str(count - sub) + ".ans", "w") as f:
                f.write(out)
        count += 1
