def Questions():
    lib2builtinfuctions = {

        'abs(x)':
        "Return the absolute value of number x. If the argument is a complex number, its magnitude is returned.",

        'all(iterable)':
        "Return True if all elements of the iterable are true (or if the iterable is empty)",

        'any(iterable)':
        "Return True if any element of the iterable is true. If the iterable is empty, return False.",

        'ascii(object)':
        "Return a string containing characters in an object, but escape the non-ASCII characters using \.",

        'bin(x)':
        "Convert an integer number to a binary string prefixed with “0b”. The result is a valid Python expression. If x is not a Python int object, it has to define an __index__() method that returns an integer.",

        'bool([x])':
        "Return a Boolean value of x or False if no argument.",

        'callable(object)':
        "Return True if the object argument appears callable, False if not. If this returns true, it is still possible that a call fails, but if it is false, calling object will never succeed. Note that classes are callable (calling a class returns a new instance); instances are callable if their class has a __call__() method.",

        'chr(i)':
        "Return the string representing a character whose Unicode code point is the integer i. ValueError will be raised if i is outside that range.",

        'compile()':
        "NO ARGS*INCOMPLETE. Compile the source into a code or AST object. Code objects can be executed by exec() or eval(). source can either be a normal string, a byte string, or an AST object. Refer to the ast module documentation for information on how to work with AST objects.",

        'delattr(object, name)':
        "The function deletes the name attribute from object, provided the object allows it. This is a relative of setattr(). The arguments are an object and a string. The string must be the name of one of the object’s attributes.",

        'dir([object])':
        "Return a list of valid attributes for an object, or the list of names in the current local scope if no argument.",

        'eval(expression)':
        "The expression argument string is parsed and evaluated as a Python expression",

        'exec(object)':
        "Dynamic execution of Python code object.",

        'filter(function, iterable)':
        "Construct an iterator from those elements of iterable for which function returns true. iterable may be either a sequence, a container which supports iteration, or an iterator. If function is None, the identity function is assumed, that is, all elements of iterable that are false are removed.",

        'float([x])':
        "Return a floating point number constructed from a number or string x, or 0.0 if no argument.",

        'getattr(object, name)':
        "Return the value of the name attribute of object.",

        'globals()':
        "Return a dictionary representing the current global symbol table. This is always the dictionary of the current module (inside a function or method, this is the module where it is defined, not the module from which it is called).",

        'hasattr(object, name)':
        "Check if object has name attribute, return True or False.",

        'hash(object)':
        "Return the hash value of an object (if it has one).",

        'help([object])':
        "Invoke the built-in help system. (This function is intended for interactive use.) If no argument is given, the interactive help system starts on the interpreter console. If the argument is a string, then the string is looked up as the name of a module, function, class, method, keyword, or documentation topic, and a help page is printed on the console. If the argument is any other kind of object, a help page on the object is generated.",

        'hex(x)':
        "Convert an integer number x to a lowercase hexadecimal string prefixed with “0x”. If x is not a Python int object, it has to define an __index__() method that returns an integer. Some examples:",

        'id(object)':
        "Return the “identity” of an object. This is an integer which is guaranteed to be unique and constant for this object during its lifetime. Two objects with non-overlapping lifetimes may have the same value.",

        'input([prompt])':
        "Takes input from the user, with or without a prompt.",

        'instance(object, classinfo)':
        "Return true if the object argument is an instance of the classinfo argument, or of a (direct, indirect or virtual) subclass thereof. If object is not an object of the given type, the function always returns false. If classinfo is a tuple of type objects (or recursively, other such tuples), return true if object is an instance of any of the types. If classinfo is not a type or tuple of types and such tuples, a TypeError exception is raised.",

        'issubclass(class, classinfo)':
        "Return true if class is a subclass (direct, indirect or virtual) of classinfo. A class is considered a subclass of itself. classinfo may be a tuple of class objects, in which case every entry in classinfo will be checked. In any other case, a TypeError exception is raised.",

        'len(s)':
        "Return the length (the number of items) of a sequence object. The argument may be a sequence (such as a string, bytes, tuple, list, or range) or a collection (such as a dictionary, set, or frozen set).",

        'list([iterable])':
        "Return a list object of an iterable, or blank list.",

        'locals()':
        "Update and return a dictionary representing the current local symbol table. Free variables are returned by locals() when it is called in function blocks, but not in class blocks.",

        'map(function, iterable)':
        "Return an iterator that applies function to every item of iterable, yielding the results. If additional iterable arguments are passed, function must take that many arguments and is applied to the items from all iterables in parallel. With multiple iterables, the iterator stops when the shortest iterable is exhausted. For cases where the function inputs are already arranged into argument tuples, see itertools.starmap().",

        'max(iterable)':
        "Return the largest item in an iterable.",

        'max(arg1, arg2, *args)':
        "Return the largest of two or more arguments",

        'memoryview(object)':
        "Return a 'memory view' object created from the given object.",

        'min(iterable)':
        "Return the smallest item in iterable.",

        'min(arg1, arg2, *args)':
        "Return the smallest of two or more arguments.",

        'next(iterator[, default])':
        "Retrieve the next item from the iterator by calling its __next__() method. If default is given, it is returned if the iterator is exhausted, otherwise StopIteration is raised.",

        'object':
        "Return a new featureless object. object is a base for all classes. It has the methods that are common to all instances of Python classes. This function does not accept any arguments.",

        'oct(x)':
        "Convert an integer number to an octal string prefixed with “0o”. The result is a valid Python expression. If x is not a Python int object, it has to define an __index__() method that returns an integer.",

        'open(file)':
        "Open file and return a corresponding file object. If the file cannot be opened, an OSError is raised.",

        'ord(c)':
        "Return an integer representing the Unicode code point of a character c."

        }
    lib4builtintypes = {

        'x in s':
        "Return True if item x is equal to an item in sequence.",

        'x not in s':
        "Return False if item x is equal to an item in sequence.",

        's + t':
        "Concatenate sequences s and t.",

        's * n':
        "Add sequence to itself n times.",

        's[i:j]':
        "Return slice of sequence from i to j.",

        's[i:j:k]':
        "Return slice of sequence from i to j, with step k",

        's.index(x[, i[, j]])':
        "Return index of first occurrence of x in sequence (at or after i and before j)",

        's.count(x)':
        "Return number of occurrences of x in sequence.",

        's[i] = x':
        "Replace item in sequence at index i with x.",

        's[i:j] = t':
        "Replace slice in sequence between i and j with t.",

        'del s[i:j]':
        "Delete slice in sequence between i and j.",

        's.append(x)':
        "Append x to sequence.",

        's.clear()':
        "Remove all items in sequence.",

        's.copy()':
        "Return shallow copy of sequence.",

        's.extend(t)':
        "Extend sequence with contents of t.",

        's *= n':
        "Update sequence with its contents repeated n times",

        's.insert(i, x)':
        "Insert x into sequence at index i",

        's.pop([i])':
        "Remove and return item at index i, or last item in sequence.",

        's.remove(x)':
        "Remove first item in sequence equal to x.",

        's.reverse()':
        "Reverses the items of sequence.",

        's.sort()':
        "Sort the sequence",

        'range(i, j[, k])':
        "Return list between i and j with optional step k.",

        'range(i)':
        "Return list from 0 to i.",

        'str(object)':
        "Return string version of object."

        }
    plr7simplestatements = {

        'assert expression':
        "Raise Assertion error if expression is false",

        'pass':
        "A null operation, nothing happens.",

        'del':
        "Delete something recursively - a list, variable name, attribute references, etc."

        }
    plr8compoundstatements = {

        'if expression:':
        "If expression is True, execute code after - efif expression: and else: are optional",

        'while expression:':
        "Repeatedly execute code if expression is True - else: will execute on termination and is optional.",

        'for target_list in expression_list:':
        "Iterates through expression_list, assigning each item as target_list, and executing the block of code."

        }

    questions = {}
    for dictionary in list(dir()):
        questions.update(eval(dictionary+".items()"))
    return questions
