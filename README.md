# StacklessBrainfuck
A brainfuck implementation that does not use a stack for the brackets

## How it works
Whenever a bracket is encountered, a counter is incremented or decremted.

If the bracket matches its condition to skip to its equivalent, the program is iterated over until a bracket with the same index is found.

## But does it work?
I've successfully run two programs.
- The [Hello World!](https://en.wikipedia.org/wiki/Brainfuck#Hello_World!) linked on the [Brainfuck Wikipedia article](https://en.wikipedia.org/wiki/Brainfuck)
- This [Mandelbrot Visualizer](https://github.com/queue-miscreant/mandelbrot-brainfuck) written in Brainfuck
- A few programs from [some brainfuck fluff](http://www.brainfuck.org/)
    - [fib.b](http://www.brainfuck.org/fib.b)
    - [sierpinski.b](http://www.brainfuck.org/sierpinski.b)
    - Others may run too, but I cannot tell how they're supposed to work or I didn't test them

Which I'd say is functional enough!

## But what for? Why?
Simply because I had the idea. Plus this may be useful if I ever wanted to build a brainfuck machine with as little memory as possible.

Frankly, even I'm surprised this actually works!

I got the idea a few years back while I was watching a school acquaintence work on their own brainfuck interpreter, and struggle with the brackets quite a bit. Admittedly, that guy was doing it in ANSI C, if I recall correctly.

## Are you the first one with this idea?
After looking around a bit, no. Someone had done this exact same idea already.
[Shoutout to jhoviatt!](https://github.com/jhoviatt/bfi)

But this idea was enough of a burning question for me to want to implement regardless.