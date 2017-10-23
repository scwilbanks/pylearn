def Questions():

    mdnbuiltinobjects = {

        'arr.length':
        "Return length property of arr array.",

        'Array.from(arrayLike[, mapFn[, thisArg]])':
        "Return a new Array instance from an arrayLike, optional mapFn and thisArg.",

        'Array.of([element1[, *elements]])':
        "Return new Array of at least one element",

        "arr.concat(arr2)":
        "Return new array from concatenating arr and arr2.",

        'arr.filter(callback[, thisArg])':
        "Return new array with all elements that pass the callback function, optional thisArg.",

        'arr.find(callback[, thisArg])':
        "Returns the value of the first element in the array that satisfies the callback function, optional thisArg. Otherwise returns undefined.",

        'arr.findIndex(callback[, thisArg])':
        "Return the index of the first element in array that satisfies the callback, optional thisArg. Otherwise returns -1.",

        'arr.join([seperator])':
        "Return string of all elements of an array-like object joined together with optional seperator.",

        'arr.pop()':
        "Remove and return last element from arr.",

        'arr.push([element1[, *elements]])':
        "Add one or more elements to end of arr and returns new length of array.",

        'arr.reverse()':
        "Reverse arr in place and returns reference to array.",

        'arr.shift()':
        "Remove and return first element of arr.",

        'arr.slice([begin[, end]])':
        "Return a shallow copy of elements from arr at optional begin to end indexes.",

        'arr.sort([compareFunction])':
        "Sort arr in place and return the sorted arr, optional compareFunction.",

        'arr.splice(start[, deleteCount[, *items]])':
        "Modify arr to remove deleteCount items at index start, and add *items. Both deleting and adding are optional. Returns deleted elements.",

        'arr.toString()':
        "Returns string of items in arr joined with commas.",

        'arr.unshift([element1[, *elements]])':
        "Add one or more elements to beginning of arr and return new length of arr.",

        'arr.values()':
        "Return new Array Iterator object that contains the values for each index in arr."
        }
    mdnstatementsanddeclarations = {

        'if (condition)':
        "Execute a statement if a specified condition is truthy. If the condition is falsy, another statment can be executed.",

        'switch (expression)':
        "Evaluate an expression, matching the expression's value to a case class, and executes statements associated with that case.",

        'var':
        "Declare a variable, optionally initializing it to a value.",

        'let':
        "Declare a block scope local variable, optionally initializing it to a value.",

        'const':
        "Declares a read-only named constant.",

        'function name([*parameters])':
        "Define a function, optionally with specified parameters.",

        'class name [extends another]':
        "Declare a new class with given name, optionally as a child of another class.",

        'for ([initialization]; [condition]; [final-expression])':
        "Create a loop that consists of three optional expressions, initialization, condition, and final-expression.",

        'for (variable in object)':
        "Iterates over the enumerable properties (variable) of an object, in original insertion order.",

        'import':
        "Import bindings which are exported by another module."

        }

    questions = {}
    for dictionary in list(dir()):
        questions.update(eval(dictionary+".items()"))
    return questions
