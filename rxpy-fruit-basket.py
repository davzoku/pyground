from rx import Observable, Observer
# Using rx to buy cheap fruits and veg for less than $5 each by generating 2 observable sequences and merge the result

# create array
fruit_basket =[
	 {'name' : 'apple', 'price': 3},
     {'name' : 'orange', 'price': 5},
     {'name' : 'pineapple', 'price': 7},
]

veg_basket =[
	 {'name' : 'bean', 'price': 2},
     {'name' : 'pea', 'price': 6},
     {'name' : 'leek', 'price': 2},
]

# buyFruit iterate through array and call on_next() when fruits are cheap
def buyFruit(observer):
    for fruit in fruit_basket:
    	if fruit['price'] <= 5:
        	observer.on_next(fruit['name'])
    observer.on_completed()
    
def buyVeg(observer):
    for veg in veg_basket:
    	if veg['price'] <= 5:
        	observer.on_next(veg['name'])
    observer.on_completed()
        
class PrintObserver(Observer):
    def on_next(self, value):
        print("Buy {0}".format(value))

    def on_completed(self):
        print("Yes! We bought cheap stuff!")

    def on_error(self, error):
        print("Error Occurred: {0}".format(error))

# Generate observable sequences
fruitSource = Observable.create(buyFruit)
vegSource = Observable.create(buyVeg)

#merge 2 sequence and print results
mergeSource = fruitSource.merge(vegSource).subscribe(PrintObserver())

# Subscribe to single source
#fruitSource.subscribe(PrintObserver())
