# In the following, I use PyQt5 to build a GUI app
![Start_Window](https://user-images.githubusercontent.com/24194591/65226009-23abfe00-da94-11e9-9ff9-582f41eb8769.png)
![Calculator_Window](https://user-images.githubusercontent.com/24194591/65226061-39212800-da94-11e9-8cd3-9ab7d939011b.png)


## Challenges:
- Swapping Windows
- Working with Signals and Slots

## Upcoming Updates:
* Calculator Functionality
* More Utilities
* Automatic window close when swapping
* Limit to how many times current window can be opened

### Notes:
Swapping can be done by using seperate show() methods; however, 
the program crashes on running multiple exec_ methods from
QApplication class. You should only have 1 exec_ method because
it runs the main function.
