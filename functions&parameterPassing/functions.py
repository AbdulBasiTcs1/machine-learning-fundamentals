# 1️⃣ Functions
def function_name(parameters):
    # code
    return value

def add(a, b):
    return a + b

print(add(2, 3))  # 5


# 2️⃣ Parameters vs Arguments

def greet(name):   # parameter
    print("Hello", name)

greet("Basit")     # argument


# 3️⃣ Types of Parameter Passing (Python)
# ✅ a) Positional Arguments
def sub(a, b):
    print(a - b)

sub(10, 5)


# ✅ b) Keyword Arguments
sub(b=5, a=10)

# ✅ c) Default Parameters
def greet(name="User"):
    print("Hello", name)

greet()
greet("Basit")

# ✅ d) Variable Length Arguments
def total(*nums):
    return sum(nums)

print(total(1, 2, 3))


# 4️⃣ Parameter Passing Behavior
def update(lst):
    lst.append(10)

my_list = [1, 2]
update(my_list)
print(my_list)  # [1, 2, 10]
