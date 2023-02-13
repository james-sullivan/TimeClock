# Time Clock CLI

Use ``python main.py --help `` for full command options

```
Commands:
  {create_user,start_shift,end_shift,start_break,end_break,start_lunch,end_lunch,print_record}
    create_user         Create a new user
    start_shift         Start a users shift
    end_shift           End a users shift
    start_break         Start a users break
    end_break           End a users break
    start_lunch         Start a users lunch
    end_lunch           End a users lunch
    print_record        Prints the record of a users past shifts, lunches, and breaks
```

Example: 

To create a new user ``python main.py create_user ``

``New user with id c409fff0-97e8-4b3a-aa12-39598e4a9558 was created``

To start a shift for that user ``python main.py start_shift  --id c409fff0-97e8-4b3a-aa12-39598e4a9558``

``User with id c409fff0-97e8-4b3a-aa12-39598e4a9558 started shift at time 2023-02-13T01:26:37``