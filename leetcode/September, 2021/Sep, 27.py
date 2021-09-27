# Unique Email Addresses

# Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.
#     For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
# If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.
#     For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
# If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.
#     For example, "m.y+name@email.com" will be forwarded to "my@email.com".
# It is possible to use both of these rules at the same time.
# Given an array of strings emails where we send one email to each email[i], return the number of different addresses that actually receive mails.

# Example 1:

# Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# Output: 2
# Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.

class Solution:
    def numUniqueEmails(self, emails):
        def checkName(name):
            name = name.replace(".", "").split("+", 1)
            return name[0]

        validMail = set([])
        for email in emails:
            [name, mail] = self.splitMail(email)
            name = checkName(name)
            print(name, mail)
            if name!=None:
                validMail.add(name+'@'+mail)
        return len(validMail)

    def splitMail(self, email):
        try:
            name, mail = email.split('@')
            return [name, mail]
        except ValueError():
            return




if __name__ == '__main__':
    sol = Solution()
    emails = ["test.email+alex@leetcode.com","test.email.leet+alex@code.com"]
    print(sol.numUniqueEmails(emails))