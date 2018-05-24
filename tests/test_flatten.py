import unittest

import flatten_json

class TestFlattenJSON(unittest.TestCase):
    def setUp(self):
        self.json_string = open('./tests/complex.json').read()

    def test_flatten_complex(self):
        actual = flatten_json.flatten_json(self.json_string)
        expected = {
            'Records.0.ses.mail.headers.2.value': 'v=1; a=rsa-sha256; c=relaxed/relaxed; d=example.com; s=example; h=mime-version:from:date:message-id:subject:to:content-type; bh=jX3F0bCAI7sIbkHyy3mLYO28ieDQz2R0P8HwQkklFj4=; b=sQwJ+LMe9RjkesGu+vqU56asvMhrLRRYrWCbV',
            'Records.0.ses.mail.commonHeaders.returnPath': 'janedoe@example.com',
            'Records.0.ses.mail.messageId': 'o3vrnil0e2ic28tr',
            'Records.0.ses.receipt.action.type': 'Lambda',
            'Records.0.ses.mail.headers.3.name': 'MIME-Version',
            'Records.0.ses.mail.source': 'janedoe@example.com',
            'Records.0.ses.receipt.virusVerdict.status': 'PASS',
            'Records.0.ses.mail.headers.7.name': 'Subject',
            'Records.0.ses.mail.headers.9.name': 'Content-Type',
            'Records.0.ses.mail.commonHeaders.messageId': '<0123456789example.com>',
            'Records.0.ses.mail.headers.0.name': 'Return-Path',
            'Records.0.ses.mail.headers.9.value': 'text/plain; charset=UTF-8',
            'Records.0.ses.mail.headers.7.value': 'Test Subject',
            'Records.0.ses.mail.headers.0.value': '<janedoe@example.com>',
            'Records.0.ses.mail.headers.4.value': 'Jane Doe <janedoe@example.com>',
            'Records.0.ses.receipt.action.invocationType': 'Event',
            'Records.0.ses.receipt.dkimVerdict.status': 'PASS',
            'Records.0.ses.mail.headers.8.name': 'To',
            'Records.0.ses.mail.headers.6.value': '<0123456789example.com>',
            'Records.0.eventSource': 'aws:ses',
            'Records.0.ses.mail.headers.4.name': 'From',
            'Records.0.ses.receipt.processingTimeMillis': '574',
            'Records.0.ses.mail.headersTruncated': 'False',
            'Records.0.ses.mail.commonHeaders.date': 'Wed, 7 Oct 2015 12:34:56 -0700',
            'Records.0.ses.receipt.spfVerdict.status': 'PASS',
            'Records.0.ses.mail.headers.2.name': 'DKIM-Signature',
            'Records.0.ses.mail.destination.0': 'johndoe@example.com',
            'Records.0.ses.receipt.recipients.0': 'johndoe@example.com',
            'Records.0.ses.mail.headers.5.name': 'Date',
            'Records.0.ses.receipt.action.functionArn': 'arn:aws:lambda:us-west-2:012345678912:function:Example',
            'Records.0.ses.mail.headers.8.value': 'johndoe@example.com',
            'Records.0.ses.mail.headers.5.value': 'Wed, 7 Oct 2015 12:34:56 -0700',
            'Records.0.ses.mail.commonHeaders.subject': 'Test Subject',
            'Records.0.ses.mail.headers.1.name': 'Received',
            'Records.0.ses.mail.commonHeaders.from.0': 'Jane Doe <janedoe@example.com>',
            'Records.0.ses.mail.headers.1.value': 'from mailer.example.com (mailer.example.com [203.0.113.1]) by inbound-smtp.us-west-2.amazonaws.com with SMTP id o3vrnil0e2ic for johndoe@example.com; Wed, 07 Oct 2015 12:34:56 +0000 (UTC)',
            'Records.0.eventVersion': '1.0',
            'Records.0.ses.mail.headers.3.value': '1.0',
            'Records.0.ses.mail.headers.6.name': 'Message-ID',
            'Records.0.ses.receipt.timestamp': '1970-01-01T00:00:00.000Z',
            'Records.0.ses.mail.commonHeaders.to.0': 'johndoe@example.com',
            'Records.0.ses.receipt.spamVerdict.status': 'PASS',
            'Records.0.ses.mail.timestamp': '1970-01-01T00:00:00.000Z'
        }
        self.assertEqual(actual, expected)

    def test_flatten_simple(self):
        simple = '{"a":1,"b":"c"}'
        actual = flatten_json.flatten_json(simple)
        expected = {
            'a': '1',
            'b': 'c',
        }
        self.assertEqual(actual, expected)

    def test_flatten_simple_list(self):
        simple = '[1,2,4]'
        actual = flatten_json.flatten_json(simple)
        expected = {'1': '2', '0': '1', '2': '4'}
        self.assertEqual(actual, expected)

    def test_flatten_escaped(self):
        simple = '{"x.y":1,"b":"c"}'
        actual = flatten_json.flatten_json(simple)
        expected = {
            'x\.y': '1',
            'b': 'c',
        }
        self.assertEqual(actual, expected)

    def test_flatten_this(self):
        simple = '{"x.y":[{"x.1":1, "n":{"a":1, "b":2}},   {"k":"l"}],"b":"c", "0":1}'
        actual = flatten_json.flatten_json(simple)
        expected = {
            'b': 'c',
            'x\\.y.0.n.a': '1',
            'x\\.y.0.n.b': '2',
            'x\\.y.0.x\\.1': '1',
            'x\\.y.1.k': 'l',
            '0': '1',
        }
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
