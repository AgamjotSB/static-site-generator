import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello world!",
            None,
            {"class": "greeting", "href": "https://github.com/AgamjotSB"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://github.com/AgamjotSB"',
        )

    def test_values(self):
        node = HTMLNode("div", "this is a value test")
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "this is a value test")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_repr(self):
        node = HTMLNode("h2", "Massive Heading", None, {"class": "heading"})
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(h2, Massive Heading, children: None, props: {'class': 'heading'})",
        )

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "here's a link", {"href": "https://github.com/AgamjotSB"})
        self.assertEqual(
            node.to_html(), '<a href="https://github.com/AgamjotSB">here\'s a link</a>'
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "testing text")
        self.assertEqual(node.to_html(), "testing text")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_multiple_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "Italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p>",
        )
