# Project_Euler
Solutions to problems in Project Euler

This is my attempt at solving the problems posted on Project Euler. There are 600+ of them, so this will probably continue for several years. But I wish to solve the first 50 at least, and then select the ones that sound interesting. I will also try commenting my thought process while solving each problem. I don't know exactly why I am doing this. It sounds fun and challenging. I guess that is enought to get me going.

Problem 1. Multiples of 3 and 5.

        Start date: 3rd of April. 2018. Tuesday.
        Solution: 233168
        End date: 3rd of April. 2018. Tuesday.


        First try. Let's see how it goes.
        Completed in under a minute. Simple use for loop and modulus.


Problem 2. Fibbonacci.

		Start date: 3rd of April. 2018. Tuesday.
		Solution: 461372
		End date: 3rd of April. 2018. Tuesday.



		Simple enough too. I decided to create an array of Fibbonacci using a while loop and added all the even sums.
		I wanted to try recurssion for this. But I'll do that for the next Fibbo assignment.


Problem 3. Largest prime factor.

		Start date: 3rd of April. 2018. Tuesday.
		Solution: 6857
		End date: 5th of April. 2018. Thursday.



		I wanted to try something other than the brute force method. Something more efficient.
		Also note that I won't use any information that can be found on the internet easily, say list of prime numbers. At least not for this.
		I was thinking something on the terms that if a number is not divisible by 2, then the
		biggest prime factor of x cannot be larger than x/3. (since the next possible factor would be 3, and it's corresponding factor x/3)
		Similarly if x does not have 3 as its factor, then the biggest prime factor cannot be larger than x/5.
		This way I can reduce the domain of search every time I check if a prime number is a factor or not.
		This method requires me to get or generate a list of prime numbers in an ascending order and check for every single one. However, I want to approach from a more efficient standpoint in terms of work that python has to do.

		I think I am going to write a script to prime factorize any given natural number and simply find the largest factor in the list containing the factors.
		Yeah, I ended up doing that. It was a simple recursive function to factorize it. Using the function also ended up giving me the factors in ascending order, so there was no need to look up the largest number. And now I have a way to factorize any number. Nice.


Problem 4. Largest palindrome product.

		Start date: 5th of April. 2018. Thursday.
		Solution: 6857
		End date: 6th of April. 2018. Friday.



		First thought is that this is heavily based on brute force. There is no other way around it. Either start multiplying largest 3-digit numbers and check if the product is palindrome or not. And even then I will need to check that the product is the largest there is (that is, I can't go on checking 999*999, 999*998, 999*997, ... 999*1).

		Oh wait. This gives me some idea. Since the order of the numbers doesn't matter, I can reduce the range that need to be searched for by enforcing the first number to be larger than the second.

		But I still would need to check for larger products (which will also need to be found through brute force) once I have found the first palindrome number. Nope. I want something more efficient.

		Note that the palindrome would be a 6 digit number or less. Perhaps palindromes have some property about its factors. Need to look into that.