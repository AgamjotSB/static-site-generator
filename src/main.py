from textnode import TextNode, TextType


def main():
    obj = TextNode("This is some anchor text", TextType.IMAGE, "https://www.ok.com")
    print(obj)


main()
