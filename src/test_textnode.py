import unittest

from textnode import TextNode, TextType, text_node_to_html_node


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


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)

        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.children, None)
        self.assertEqual(html_node.props, None)

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.image.com")
        html_node = text_node_to_html_node(node)

        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props, {"src": "https://www.image.com", "alt": "This is an image"}
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)

        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

    def test_italic(self):
        node = TextNode("This is italic", TextType.ITALIC)
        html_node = text_node_to_html_node(node)

        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is italic")

    def test_link(self):
        node = TextNode("This is a link", TextType.LINK, "https://www.link.com")
        html_node = text_node_to_html_node(node)

        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link")
        self.assertEqual(html_node.props, {"href": "https://www.link.com"})


if __name__ == "__main__":
    unittest.main()
