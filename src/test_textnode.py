import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a textnode", TextType.TEXT)
        node2 = TextNode("This is a textnode", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq2(self):
        node = TextNode("This is a textnode", TextType.TEXT)
        node2 = TextNode("This is a different textnode", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_url_eq(self):
        node = TextNode("link go brr", TextType.LINK, "https://www.ok.com")
        node2 = TextNode("link go brr", TextType.LINK, "https://www.ok.com")
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
