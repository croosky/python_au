import unittest
import json
from request import *


class TestRequest(unittest.TestCase):
  def test_get_all_pullrequests(self):
    result=get_all_pullrequest('croosky','python_au','all')
    file = open('pulls.json','r')
    expect=json.load(file)
    self.assertEqual(result,expect)
  def test_get_all_commits(self):
    file = open('pulls.json','r')
    pull_request=json.load(file)[-1]
    result=get_all_commits(pull_request)
    expect=['?', 'LEETCODE-1021 Added Linked list', 'Delete r.txt']
    self.assertEqual(result,expect)
  def test_commit_verification(self):
    wrong_title='Leetcode-1023 tree'
    right_title='LEETCODE-1021 Added something'
    expect_wrong='Prefix should be one of the: LEETCODE, GENERATOR, HEXNUMBER, TRIANGLE, ITERATOR, REQUESTS\nGroup should be one of the: 1021, 1022\nAction should be one of the: Added, Fixed, Refactored, Deleted, Moved'
    expect_right=''
    self.assertEqual(commit_verification(wrong_title),expect_wrong)
    self.assertEqual(commit_verification(right_title),expect_right)
  #def test_send_error_messages(self):
   # result=
    #expect=
    #self.assertEqual(result,expect)
  def test_check_oldness(self):
    file=open('pulls.json','r')
    pr_with_comments=json.load(file)[-1]
    pr_without=json.load(file)[-10]
    self.assertEqual(check_pldness(pr_with_comments),True)
    self.assertEqual(check_pldness(pr_without),False)
