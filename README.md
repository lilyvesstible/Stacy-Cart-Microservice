Hello! This is a simple cart program, where you can add, delete, and view items in a cart.

Request data via a single string. The string should have three sections, separated by a comma. Although not all operations will require all three values, you must include all three values every time.
The first value is the Item ID. This determines the item that's being modified.
The second value is the quantity of items being modified.
The third value is the operation being performed.

Receive data via a single string. Most operations will output a string surrounded in brackets. These strings aren't data, but just serve as confirmation to the user that the operation was successful. The View List operation will output the list.

There are 5 operations that can be performed, as listed here:
0 (Add Item): This adds an item to the list. The string output is [ITEM ADDED]. Uses all three inputs.
1 (Delete Item): This deletes an item from the list. The string output is [ITEM DELETED]. Uses all three inputs. If you try to delete more items than there are in the list, it will just delete all of them.
2 (Clear List): This clears the current list. The string output is [LIST CLEARED]. Only uses the operation input.
3 (View List): This turns the list into a string, to be sent to the user. The string output will contain all items in the list, separated by a comma.
4 (Quit): This shuts down the server. The string output is [QUIT]. Only uses the operation input
For operations 2, 3, and 4, the first two values do not matter. They can be any value, as long as they are an integer.

EX: The command "24, 3, 0" will add the number 24 to the list three times. If the list were empty, it would look like [24, 24, 24].

EX: For a list [24, 24, 5], the command "24, 6, 1" would delete 6 items with the id 24 from the list. Because there are less than 6 items, it deletes all items with the id 24. The resulting list would be [5].

EX: For a list [3, 5, 3, 24], the command "0, 0, 3" would output the string "3, 5, 3, 24". In this scenario, the first and second arguments could be any integer, though I chose 0.

Note! A server can only hold one cart at a time, and once the server is shut down, the cart is also deleted.

[UML Diagram](./UML-Microservice.drawio.png)