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

        'bytearray([source[, encoding[, errors]]])':
        "Return a new array of bytes with optional arguments encoding and errors. Returns array of length 0 if no source.",

        'bytes([source[, encoding[, errors]]])':
        "Return a new bytes object, with optional source, encoding, and errors.\n\nBytes is an immutable sequence of integers in the range 0 <= x < 256. bytes is an immutable version of bytearray – it has the same non-mutating methods and the same indexing and slicing behavior.Accordingly, constructor arguments are interpreted as for bytearray().",

        'callable(object)':
        "Return True if the object argument appears callable, False if not. If this returns true, it is still possible that a call fails, but if it is false, calling object will never succeed. Note that classes are callable (calling a class returns a new instance); instances are callable if their class has a __call__() method.",

        'chr(i)':
        "Return the string representing a character whose Unicode code point is the integer i. ValueError will be raised if i is outside that range.",

        '@classmethod':
        "Transform a method into a class method. A classmethod recieves the class as implicit first argument, just like an instance method receives the instance.",

        'compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)':
        """Compile the source code into a code or AST object from filename file with mode, and keyword arguments flags, dont_inherit, and optimize.\n\nCode objects can be executed by exec() or eval(). source can either be a normal string, a byte string, or an AST object. Refer to the ast module documentation for information on how to work with AST objects.\n\nThe filename argument should give the file from which the code was read; pass some recognizable value if it wasn’t read from a file ('<string>' is commonly used).\n\nThe mode argument specifies what kind of code must be compiled; it can be 'exec' if source consists of a sequence of statements, 'eval' if it consists of a single expression, or 'single' if it consists of a single interactive statement (in the latter case, expression statements that evaluate to something other than None will be printed).\n\nThe optional arguments flags and dont_inherit control which future statements (see PEP 236) affect the compilation of source. If neither is present (or both are zero) the code is compiled with those future statements that are in effect in the code that is calling compile(). If the flags argument is given and dont_inherit is not (or is zero) then the future statements specified by the flags argument are used in addition to those that would be used anyway. If dont_inherit is a non-zero integer then the flags argument is it – the future statements in effect around the call to compile are ignored.\n\nFuture statements are specified by bits which can be bitwise ORed together to specify multiple statements. The bitfield required to specify a given feature can be found as the compiler_flag attribute on the _Feature instance in the __future__ module.\n\nThe argument optimize specifies the optimization level of the compiler; the default value of -1 selects the optimization level of the interpreter as given by -O options. Explicit levels are 0 (no optimization; __debug__ is true), 1 (asserts are removed, __debug__ is false) or 2 (docstrings are removed too).\n\nThis function raises SyntaxError if the compiled source is invalid, and ValueError if the source contains null bytes.\n\nIf you want to parse Python code into its AST representation, see ast.parse().\n\nNote When compiling a string with multi-line code in 'single' or 'eval' mode, input must be terminated by at least one newline character. This is to facilitate detection of incomplete and complete statements in the code module.""",

        'complex([real[, imag]])':
        """Return a complex number with the value real + imag*1j or convert a string or number to a complex number. If the first parameter is a string, it will be interpreted as a complex number and the function must be called without a second parameter. The second parameter can never be a string. Each argument may be any numeric type (including complex). If imag is omitted, it defaults to zero and the constructor serves as a numeric conversion like int and float. If both arguments are omitted, returns 0j.

        Note When converting from a string, the string must not contain whitespace around the central + or - operator. For example, complex('1+2j') is fine, but complex('1 + 2j') raises ValueError.""",

        'delattr(object, name)':
        "The function deletes the name attribute from object, provided the object allows it. This is a relative of setattr(). The arguments are an object and a string. The string must be the name of one of the object’s attributes.",

        'dir([object])':
        "Return a list of valid attributes for an object, or the list of names in the current local scope if no argument.",

        'divmod(a, b)':
        "Take two (non complex) numbers a and b and return a pair of numbers consisting of their quotient and remainder when using integer division.\n\nWith mixed operand types, the rules for binary arithmetic operators apply. For integers, the result is the same as (a // b, a % b). For floating point numbers the result is (q, a % b), where q is usually math.floor(a / b) but may be 1 less than that. In any case q * b + a % b is very close to a, if a % b is non-zero it has the same sign as b, and 0 <= abs(a % b) < abs(b).",

        'enumerate(iterable, start=0)':
        "Return an enumerate object of iterable at keyword argument start.\n\n iterable must be a sequence, an iterator, or some other object which supports iteration. The __next__() method of the iterator returned by enumerate() returns a tuple containing a count (from start which defaults to 0) and the values obtained from iterating over iterable.",

        'eval(expression, globals=None, locals=None)':
        "The expression argument string is parsed and evaluated as a Python expression, with keyword arguments globals and locals.\n\nThe arguments are a string and optional globals and locals. If provided, globals must be a dictionary. If provided, locals can be any mapping object.\n\nThe expression argument is parsed and evaluated as a Python expression (technically speaking, a condition list) using the globals and locals dictionaries as global and local namespace. If the globals dictionary is present and lacks ‘__builtins__’, the current globals are copied into globals before expression is parsed. This means that expression normally has full access to the standard builtins module and restricted environments are propagated. If the locals dictionary is omitted it defaults to the globals dictionary. If both dictionaries are omitted, the expression is executed in the environment where eval() is called. The return value is the result of the evaluated expression. Syntax errors are reported as exceptions.\n\nThis function can also be used to execute arbitrary code objects (such as those created by compile()). In this case pass a code object instead of a string. If the code object has been compiled with 'exec' as the mode argument, eval()’s return value will be None.\n\nHints: dynamic execution of statements is supported by the exec() function. The globals() and locals() functions returns the current global and local dictionary, respectively, which may be useful to pass around for use by eval() or exec().\n\nSee ast.literal_eval() for a function that can safely evaluate strings with expressions containing only literals.",

        'exec(object[, globals[, locals]])':
        "Dynamically execute of Python code object with optional globals and locals.\n\nobject must be either a string or a code object. If it is a string, the string is parsed as a suite of Python statements which is then executed (unless a syntax error occurs). [1] If it is a code object, it is simply executed. In all cases, the code that’s executed is expected to be valid as file input (see the section “File input” in the Reference Manual). Be aware that the return and yield statements may not be used outside of function definitions even within the context of code passed to the exec() function. The return value is None.\n\nIn all cases, if the optional parts are omitted, the code is executed in the current scope. If only globals is provided, it must be a dictionary, which will be used for both the global and the local variables. If globals and locals are given, they are used for the global and local variables, respectively. If provided, locals can be any mapping object. Remember that at module level, globals and locals are the same dictionary. If exec gets two separate objects as globals and locals, the code will be executed as if it were embedded in a class definition.\n\nIf the globals dictionary does not contain a value for the key __builtins__, a reference to the dictionary of the built-in module builtins is inserted under that key. That way you can control what builtins are available to the executed code by inserting your own __builtins__ dictionary into globals before passing it to exec().\n\nNote The built-in functions globals() and locals() return the current global and local dictionary, respectively, which may be useful to pass around for use as the second and third argument to exec().\n\nNote The default locals act as described for function locals() below: modifications to the default locals dictionary should not be attempted. Pass an explicit locals dictionary if you need to see effects of the code on locals after function exec() returns.",

        'filter(function, iterable)':
        "Construct an iterator from those elements of iterable for which function returns true. iterable may be either a sequence, a container which supports iteration, or an iterator. If function is None, the identity function is assumed, that is, all elements of iterable that are false are removed.",

        'float([x])':
        "Return a floating point number constructed from a number or string x, or 0.0 if no argument.",

        'format(value[, format_spec])':
        """Convert a value to a “formatted” representation, as controlled by optional format_spec. The interpretation of format_spec will depend on the type of the value argument, however there is a standard formatting syntax that is used by most built-in types: Format Specification Mini-Language.

        The default format_spec is an empty string which usually gives the same effect as calling str(value).

        A call to format(value, format_spec) is translated to type(value).__format__(value, format_spec) which bypasses the instance dictionary when searching for the value’s __format__() method. A TypeError exception is raised if the method search reaches object and the format_spec is non-empty, or if either the format_spec or the return value are not strings.""",

        'frozenset([iterable])':
        "Return a new frozenset object, optionally with elements taken from iterable. frozenset is a built-in class. See frozenset and Set Types — set, frozenset for documentation about this class.",

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

        'int(x, base=y)':
        """Return an integer object from number x with keyword argument base.\n\nInt is constructed from a number or string x, or return 0 if no arguments are given. If x is a number, return x.__int__(). For floating point numbers, this truncates towards zero.

        If x is not a number or if base is given, then x must be a string, bytes, or bytearray instance representing an integer literal in radix base. Optionally, the literal can be preceded by + or - (with no space in between) and surrounded by whitespace. A base-n literal consists of the digits 0 to n-1, with a to z (or A to Z) having values 10 to 35. The default base is 10. The allowed values are 0 and 2–36. Base-2, -8, and -16 literals can be optionally prefixed with 0b/0B, 0o/0O, or 0x/0X, as with integer literals in code. Base 0 means to interpret exactly as a code literal, so that the actual base is 2, 8, 10, or 16, and so that int('010', 0) is not legal, while int('010') is, as well as int('010', 8).""",

        'isinstance(object, classinfo)':
        "Return true if the object argument is an instance of the classinfo argument, or of a (direct, indirect or virtual) subclass thereof. If object is not an object of the given type, the function always returns false. If classinfo is a tuple of type objects (or recursively, other such tuples), return true if object is an instance of any of the types. If classinfo is not a type or tuple of types and such tuples, a TypeError exception is raised.",

        'issubclass(class, classinfo)':
        "Return true if class is a subclass (direct, indirect or virtual) of classinfo. A class is considered a subclass of itself. classinfo may be a tuple of class objects, in which case every entry in classinfo will be checked. In any other case, a TypeError exception is raised.",

        'iter(object[, sentinel])':
        """Return an iterator object from object with optional sentinel.\n\nThe first argument is interpreted very differently depending on the presence of the second argument. Without a second argument, object must be a collection object which supports the iteration protocol (the __iter__() method), or it must support the sequence protocol (the __getitem__() method with integer arguments starting at 0). If it does not support either of those protocols, TypeError is raised. If the second argument, sentinel, is given, then object must be a callable object. The iterator created in this case will call object with no arguments for each call to its __next__() method; if the value returned is equal to sentinel, StopIteration will be raised, otherwise the value will be returned.

        See also Iterator Types.

        One useful application of the second form of iter() is to read lines of a file until a certain line is reached. The following example reads a file until the readline() method returns an empty string:

        with open('mydata.txt') as fp:
            for line in iter(fp.readline, ''):
                process_line(line)""",

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

        'max(arg1, arg2[, *args])':
        "Return the largest of two or more arguments",

        'memoryview(object)':
        "Return a 'memory view' object created from the given object.",

        'min(iterable)':
        "Return the smallest item in iterable.",

        'min(arg1, arg2[, *args])':
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
        "Return an integer representing the Unicode code point of a character c.",

        'pow(x, y[, z])':
        """Return x to the power y; if z is present, return x to the power y, modulo z (computed more efficiently than pow(x, y) % z). The two-argument form pow(x, y) is equivalent to using the power operator: x**y.

        The arguments must have numeric types. With mixed operand types, the coercion rules for binary arithmetic operators apply. For int operands, the result has the same type as the operands (after coercion) unless the second argument is negative; in that case, all arguments are converted to float and a float result is delivered. For example, 10**2 returns 100, but 10**-2 returns 0.01. If the second argument is negative, the third argument must be omitted. If z is present, x and y must be of integer types, and y must be non-negative.""",

        "print(*objects, sep='', end='\\n', file=sys.stdout, flush=False)":
        """Print objects to the text stream file, with keyword arguments sep, end, and flush. sep, end, file and flush, if present, must be given as keyword arguments.

        All non-keyword arguments are converted to strings like str() does and written to the stream, separated by sep and followed by end. Both sep and end must be strings; they can also be None, which means to use the default values. If no objects are given, print() will just write end.

        The file argument must be an object with a write(string) method; if it is not present or None, sys.stdout will be used. Since printed arguments are converted to text strings, print() cannot be used with binary mode file objects. For these, use file.write(...) instead.

        Whether output is buffered is usually determined by file, but if the flush keyword argument is true, the stream is forcibly flushed.""",

        'property(fget=None, fset=None, fdel=None, doc=None)':
        "Return a property attribute with fget, fset, fdel, and doc keyword arguments. fget is a function for getting an attribute value. fset is a function for setting an attribute value. fdel is a function for deleting an attribute value. And doc creates a docstring for the attribute.",

        'range(start, stop[, step])':
        "Return range from start to stop with optional step. Not a function but an immutable sequence type.",

        'repr(object)':
        "Return a string containing a printable representation of object.\n\nFor many types, this function makes an attempt to return a string that would yield an object with the same value when passed to eval(), otherwise the representation is a string enclosed in angle brackets that contains the name of the type of the object together with additional information often including the name and address of the object. A class can control what this function returns for its instances by defining a __repr__() method.",

        'reversed(seq)':
        "Return a reverse iterator. seq must be an object which has a __reversed__() method or supports the sequence protocol (the __len__() method and the __getitem__() method with integer arguments starting at 0).",

        'round(number[, ndigits])':
        """Return number rounded to ndigits precision after the decimal point. If ndigits is omitted or is None, it returns the nearest integer to its input.

        For the built-in types supporting round(), values are rounded to the closest multiple of 10 to the power minus ndigits; if two multiples are equally close, rounding is done toward the even choice (so, for example, both round(0.5) and round(-0.5) are 0, and round(1.5) is 2). Any integer value is valid for ndigits (positive, zero, or negative). The return value is an integer if called with one argument, otherwise of the same type as number.

        For a general Python object number, round(number, ndigits) delegates to number.__round__(ndigits).

        Note The behavior of round() for floats can be surprising: for example, round(2.675, 2) gives 2.67 instead of the expected 2.68. This is not a bug: it’s a result of the fact that most decimal fractions can’t be represented exactly as a float. See Floating Point Arithmetic: Issues and Limitations for more information.""",

        'set([iterable])':
        "Return a set object, optionally with elements from iterable.",

        'setattr(object, name, value)':
        "Set attribute name of object to value.\n\nThis is the counterpart of getattr(). The arguments are an object, a string and an arbitrary value. The string may name an existing attribute or a new attribute. The function assigns the value to the attribute, provided the object allows it. For example, setattr(x, 'foobar', 123) is equivalent to x.foobar = 123.",

        'slice(start, stop[, step])':
        "Return a slice object representing the set of indices specified by range(start, stop, step). The start and step arguments default to None. Slice objects have read-only data attributes start, stop and step which merely return the argument values (or their default). They have no other explicit functionality; however they are used by Numerical Python and other third party extensions. Slice objects are also generated when extended indexing syntax is used. For example: a[start:stop:step] or a[start:stop, i]. See itertools.islice() for an alternate version that returns an iterator.",

        'sorted(iterable, *, key=None, reverse=False)':
        "Return a new sorted list from the items in iterable and other iterables, with keyword arguments key and reverse.\n\nHas two optional arguments which must be specified as keyword arguments.\n\nkey specifies a function of one argument that is used to extract a comparison key from each list element: key=str.lower. The default value is None (compare the elements directly).\n\nreverse is a boolean value. If set to True, then the list elements are sorted as if each comparison were reversed.\n\nUse functools.cmp_to_key() to convert an old-style cmp function to a key function.\n\nThe built-in sorted() function is guaranteed to be stable. A sort is stable if it guarantees not to change the relative order of elements that compare equal — this is helpful for sorting in multiple passes (for example, sort by department, then by salary grade).\n\nFor sorting examples and a brief sorting tutorial, see Sorting HOW TO.",

        '@staticmethod':
        """Transform a method into a static method.

        A static method does not receive an implicit first argument. To declare a static method, use this idiom:

        class C:
            @staticmethod
            def f(arg1, arg2, ...): ...
        The @staticmethod form is a function decorator – see the description of function definitions in Function definitions for details.

        It can be called either on the class (such as C.f()) or on an instance (such as C().f()). The instance is ignored except for its class.

        Static methods in Python are similar to those found in Java or C++. Also see classmethod() for a variant that is useful for creating alternate class constructors.

        Like all decorators, it is also possible to call staticmethod as a regular function and do something with its result. This is needed in some cases where you need a reference to a function from a class body and you want to avoid the automatic transformation to instance method. For these cases, use this idiom:

        class C:
        builtin_open = staticmethod(open)
        For more information on static methods, consult the documentation on the standard type hierarchy in The standard type hierarchy.""",

        "str(object=b'', encoding='utf-8', errors='strict')":
        """Return a string version of object with encoding and errors keyword arguments.\n\nIf object is not provided, returns the empty string. Otherwise, the behavior of str() depends on whether encoding or errors is given, as follows.

        If neither encoding nor errors is given, str(object) returns object.__str__(), which is the “informal” or nicely printable string representation of object. For string objects, this is the string itself. If object does not have a __str__() method, then str() falls back to returning repr(object).

        If at least one of encoding or errors is given, object should be a bytes-like object (e.g. bytes or bytearray). In this case, if object is a bytes (or bytearray) object, then str(bytes, encoding, errors) is equivalent to bytes.decode(encoding, errors). Otherwise, the bytes object underlying the buffer object is obtained before calling bytes.decode(). See Binary Sequence Types — bytes, bytearray, memoryview and Buffer Protocol for information on buffer objects.

        Passing a bytes object to str() without the encoding or errors arguments falls under the first case of returning the informal string representation (see also the -b command-line option to Python). For example:

        >>>
        >>> str(b'Zoot!')
        "b'Zoot!'"
        For more information on the str class and its methods, see Text Sequence Type — str and the String Methods section below. To output formatted strings, see the Formatted string literals and Format String Syntax sections. In addition, see the Text Processing Services section.""",

        'sum(iterable[, start])':
        """Sums start and the items of an iterable from left to right and returns the total. start defaults to 0. The iterable’s items are normally numbers, and the start value is not allowed to be a string.

        For some use cases, there are good alternatives to sum(). The preferred, fast way to concatenate a sequence of strings is by calling ''.join(sequence). To add floating point values with extended precision, see math.fsum(). To concatenate a series of iterables, consider using itertools.chain().""",

        'super([type[, object-or-type]])':
        """Return a proxy object that delegates method calls to a parent or sibling class of type. This is useful for accessing inherited methods that have been overridden in a class. The search order is same as that used by getattr() except that the type itself is skipped.

        The __mro__ attribute of the type lists the method resolution search order used by both getattr() and super(). The attribute is dynamic and can change whenever the inheritance hierarchy is updated.

        If the second argument is omitted, the super object returned is unbound. If the second argument is an object, isinstance(obj, type) must be true. If the second argument is a type, issubclass(type2, type) must be true (this is useful for classmethods).

        There are two typical use cases for super. In a class hierarchy with single inheritance, super can be used to refer to parent classes without naming them explicitly, thus making the code more maintainable. This use closely parallels the use of super in other programming languages.

        The second use case is to support cooperative multiple inheritance in a dynamic execution environment. This use case is unique to Python and is not found in statically compiled languages or languages that only support single inheritance. This makes it possible to implement “diamond diagrams” where multiple base classes implement the same method. Good design dictates that this method have the same calling signature in every case (because the order of calls is determined at runtime, because that order adapts to changes in the class hierarchy, and because that order can include sibling classes that are unknown prior to runtime).

        For both use cases, a typical superclass call looks like this:

        class C(B):
            def method(self, arg):
                super().method(arg)    # This does the same thing as:
                                       # super(C, self).method(arg)
        Note that super() is implemented as part of the binding process for explicit dotted attribute lookups such as super().__getitem__(name). It does so by implementing its own __getattribute__() method for searching classes in a predictable order that supports cooperative multiple inheritance. Accordingly, super() is undefined for implicit lookups using statements or operators such as super()[name].

        Also note that, aside from the zero argument form, super() is not limited to use inside methods. The two argument form specifies the arguments exactly and makes the appropriate references. The zero argument form only works inside a class definition, as the compiler fills in the necessary details to correctly retrieve the class being defined, as well as accessing the current instance for ordinary methods.

        For practical suggestions on how to design cooperative classes using super(), see guide to using super().""",

        'tuple([iterable])':
        "eturn tuple of optional argument iterable.\n\nRRather than being a function, tuple is actually an immutable sequence type, as documented in Tuples and Sequence Types — list, tuple, range.",

        'type(object)':
        "Return the type of object. \n\nThe return value is a type object and generally the same object as returned by object.__class__.\n\nThe isinstance() built-in function is recommended for testing the type of an object, because it takes subclasses into account.",

        'type(name, bases, dict)':
        """Return type object of name, bases baseclass and dict. \n\n Returns a new type object. This is essentially a dynamic form of the class statement. The name string is the class name and becomes the __name__ attribute; the bases tuple itemizes the base classes and becomes the __bases__ attribute; and the dict dictionary is the namespace containing definitions for class body and is copied to a standard dictionary to become the __dict__ attribute. For example, the following two statements create identical type objects:

        >>>
        >>> class X:
        ...     a = 1
        ...
        >>> X = type('X', (object,), dict(a=1))
        See also Type Objects.

        Changed in version 3.6: Subclasses of type which don’t override type.__new__ may no longer use the one-argument form to get the type of an object.""",

        'vars([object])':
        """Return the __dict__ attribute for an object - module, class, instance, or any other object with a __dict__ attribute.

        Objects such as modules and instances have an updateable __dict__ attribute; however, other objects may have write restrictions on their __dict__ attributes (for example, classes use a types.MappingProxyType to prevent direct dictionary updates).

        Without an argument, vars() acts like locals(). Note, the locals dictionary is only useful for reads since updates to the locals dictionary are ignored.""",

        'zip(*iterables)':
        """Make an iterator that aggregates elements from each of the iterables.

        Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables. The iterator stops when the shortest input iterable is exhausted. With a single iterable argument, it returns an iterator of 1-tuples. With no arguments, it returns an empty iterator. Equivalent to:

        def zip(*iterables):
            # zip('ABCD', 'xy') --> Ax By
            sentinel = object()
            iterators = [iter(it) for it in iterables]
            while iterators:
                result = []
                for it in iterators:
                    elem = next(it, sentinel)
                    if elem is sentinel:
                        return
                    result.append(elem)
                yield tuple(result)
        The left-to-right evaluation order of the iterables is guaranteed. This makes possible an idiom for clustering a data series into n-length groups using zip(*[iter(s)]*n). This repeats the same iterator n times so that each output tuple has the result of n calls to the iterator. This has the effect of dividing the input into n-length chunks.

        zip() should only be used with unequal length inputs when you don’t care about trailing, unmatched values from the longer iterables. If those values are important, use itertools.zip_longest() instead.

        zip() in conjunction with the * operator can be used to unzip a list:

        >>>
        >>> x = [1, 2, 3]
        >>> y = [4, 5, 6]
        >>> zipped = zip(x, y)
        >>> list(zipped)
        [(1, 4), (2, 5), (3, 6)]
        >>> x2, y2 = zip(*zip(x, y))
        >>> x == list(x2) and y == list(y2)
        True"""

        }
    lib4builtintypes = {

        'x in s':
        "Return True if item x is equal to an item in sequence.",

        'x not in s':
        "Return True if item x is not equal to any item in sequence.",

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
        "Return list between integers i and j with optional step k.",

        'range(i)':
        "Return list from 0 to integer i.",

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
