string_input=input("Enter a string")
vowels="aeiouAEIOU"
consonent_count=0
vowels_count=0
for char in string_input:
   if char in vowels:
        vowels_count+=1
   else:
        consonent_count+=1
print(f"No of consonents in the given string {string_input}={consonent_count}")
print(f"No of vowels in the given string {string_input} = {vowels_count}")