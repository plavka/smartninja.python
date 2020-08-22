print("Hello, you're joining a great new Fizz Buzz game!")

end = input("Enter a number between 1 and 100: ")
end = int(end)

for num in range(1, end+1):
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)