def Questions():
    mdnwebdocshtmlelement = {

        '<a>':
        "Anchor element. Creates a hyperlink to other web pages, files, locations within the same page, email address, or any other URL.",

        '<b>':
        "Element that represents a span of text stylistically different from normal text, without conveying any special importance or relevance, and that is typically rendered in boldface.",

        '<blockquote>':
        "Element that indicates that the enclosed text is an extended quotation. Usually, this is rendered visually by indentation. A URL for the source of the quotation may be given using the cite attribute, while a text representation of the source can be given using the <cite> element.",

        '<body>':
        "Represents the content of an HTML document. There can be only one of this element in a document.",

        '<br>':
        "Element that produces a line break in text (carriage-return). It is useful for writing a poem or an address, where the division of lines is significant.",

        '<button>':
        "Element that represents a clickable button.",

        '<em>':
        "Element that marks text that has stress emphasis. It can be nested, with each lvel of nesting indicateing a greater degree of emphasis."

        }

    questions = {}
    for dictionary in list(dir()):
        questions.update(eval(dictionary+".items()"))
    return questions
