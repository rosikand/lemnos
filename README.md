# 🔖 Lemnos: CLI To-do List Manager

Lemnos is a simple program that allows one to manage a to-do list via the command-line. 

## Example 

```
$ python3 todo.py add make pasta
$ python3 todo.py show
    1. make pasta
    Number of items: 1
$ python3 todo.py complete 1
```

You can also set up a daily recurring email sent to your inbox every morning (see section below). 

## Set up

You need to have Python installed. 

1. Clone/download this repository. 
2. `cd` into the directory when using the program. 

You are good to go! You can optionally add a shebang of your Python install location to the top of `todo.py`. You can find this by typing `which python` in the command-line. Prepend that string with `#!` and add it to the top of `todo.py`. Example string: `#!/usr/bin/python3`. Then, you can simply type `./todo` to execute the program instead. To follow the reference then, just replace `python3 todo.py` with `./todo`. If you want to make this even faster, you can set up an alias of your choice. Alternatively, you can move the executable to `/usr/local/bin` which allows you to simply type the executable name to run the program. 

If you want to use the email feature, then follow the steps in the section below. 

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
    
- **Show prioritized items**:
  
  ```
  $ python3 todo.py p
  ```

- **Complete item at index 'i'**
  
  ```
  $ python3 todo.py complete i
  ```

- **Prioritize item at index `i`**:
  
  ```
  $ python3 todo.py prioritize i
  ```

- **Un-prioritize item at index `i`**:
  
  ```
  $ python3 todo.py unprioritize i
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

## Email list 

You can also use the script stored in `mail.py` to send an email of the list to yourself. You must install the dependencies first which are [yagmail](https://github.com/kootenpv/yagmail) and [hickory](https://github.com/maxhumber/hickory). Additionally, your sending email address must be a Gmail account. 

You need to replace the variables at the top with your information:

```python
# Important: variables you should define for yourself 
your_name = "Johnny Appleseed"  # Your name
send_username = "appleseed"  # Gmail address username to send the emails from
send_password = "johnny123"  # Password for sending email account 
receiving_address = "appleseed@gmail.com"  # Email address you'd like the emails to be sent to
```

Now send an email of this list by running the script: `python3 mail.py`. 

Furthermore, with the help of the [hickory](https://github.com/maxhumber/hickory) package, you can set up a recurring email sent every morning to yourself as a reminder: 

```
hickory schedule mail.py --every=@9am
```
Make sure to kill the script eventually if you no longer want to send and receive the emails: `hickory kill mail.py`. 

## Note

I recognize that there are probably many packages/programs out there that already have this functionality, but I wanted to build one from source so that I can feasibly add customizations to my personal setup as needed. Another motivation for creating this program was that the other options available are much more feature-heavy than I needed (a minimalist user experience is the main design principle here). 


## Name 

> [Hephaestus](https://en.wikipedia.org/wiki/Hephaestus) is the Greek god of blacksmiths, metalworking, carpenters, craftsmen, among others. He resides in [Lemnos](https://en.wikipedia.org/wiki/Lemnos), which, in real life, is a Greek island in the Aegean Sea. 
