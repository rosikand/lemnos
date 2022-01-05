# 🔖 Lemnos: CLI To-do List Manager

This is a simple program that allows one to manage a to-do list via the command-line. 

## Example 

```
$ python3 todo.py add make pasta
$ python3 todo.py show
    1. make pasta
    Number of items: 1
$ python3 todo.py complete 1
```

## Set up

You need to have Python installed. 

1. Clone/download this repository. 
2. `cd` into the directory when using the program. 

You are good to go! You can optionally add a shebang of your Python install location to the top of `todo.py`. You can find this by typing `which python` in the command-line. Prepend that string with `#!` and add it to the top of `todo.py`. Example string: `#!/usr/bin/python3`. Then, you can simply type `./todo` to execute the program instead. To follow the reference then, just replace `python3 todo.py` with `./todo`. 

## Reference

- **Add item to list**: 
  
  ```
  $ python3 todo.py add item
  ```

- **Show to-do list**:
  
  ```
  $ python3 todo.py show
  ```
  
  
  - or simply: 
  
    ```
    $ python3 todo.py
    ```

- **Complete item at index i**
  
  ```
  $ python3 todo.py complete i
  ```
  

- **Erase entire list**:
  
  ```
  $ python3 todo.py erase
  ```

- **Get length of list**:
  
  ```
  $ python3 todo.py len
  ```
  
### Abbreviations 
For efficiency purposes, you can simply specify the first letter of each functionality instead of the entire word. Example of adding `item` to the list. 
```
$ python3 todo.py a item
```

The program works by adding and removing content from `list.txt` so you can alternatively manage the list via that file as well. 

## Note

I recognize that there are probably many packages/programs out there that already have this functionality, but I wanted to build one from source so that I can feasibly add customizations to my personal setup as needed. Another motivation for creating this program was that the other options available are much more feature-heavy than I needed (a minimalist user experience is the main design principle here). 


## Name 

> [Hephaestus](https://en.wikipedia.org/wiki/Hephaestus) is the Greek god of blacksmiths, metalworking, carpenters, craftsmen, among others. He resides in [Lemnos](https://en.wikipedia.org/wiki/Lemnos), which, in real life, is a Greek island in the Aegean Sea. 
