import jsog
import unittest

class TestJSOG(unittest.TestCase):

	def test_serialize_reference(self):
		inner = { "foo": "bar" }
		outer = { "inner1": inner, "inner2": inner }
		encoded = jsog.encode(outer)

		inner1 = encoded['inner1']
		inner2 = encoded['inner2']

		# one has @id, one has @ref
		self.assertNotEqual('@id' in inner1, '@id' in inner2)
		self.assertNotEqual('@ref' in inner1, '@ref' in inner2)

		if '@id' in inner1:
			self.assertEqual(inner1['@id'], inner2['@ref'])
		else:
			self.assertEqual(inner1['@ref'], inner2['@id'])

	def test_deserialize_reference(self):
		JSOGIFIED = '{"@id":"1","foo":"foo","inner1":{"@id":"2","bar":"bar"},"inner2":{"@ref":"2"}}'
		parsed = jsog.loads(JSOGIFIED)

		inner1 = parsed['inner1']
		inner2 = parsed['inner2']
		self.assertTrue(inner1 is inner2)

if __name__ == '__main__':
	unittest.main()