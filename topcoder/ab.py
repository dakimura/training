#!/usr/bin/python
#-*- coding:utf-8 -*-

class AB:

    def max_value_chars(self, N):
        """
        return an array of chars that has the max value
        """
        if N%2 == 0:
            return ["A" for k in range(N/2)] + ["B" for m in range(N/2) ]
        else:
            return ["A" for k in range((N-1)/2)] + ["B" for m in range((N-1)/2)]

    def max_value(self, N):
        """
        return the max value that can be made by N chars
        """
        if N%2 == 0:
            return (N/2)*(N/2)
        else:
            return (N/2+1)*(N/2-1)

    def decrement(self, char_array):
        """
        decrement the value of the char_array and return it
        decrement by swapping the first "B" and "A" next to it.

        e.g.
        decrement( ['A','A','B','B','A'] ) = ['A','B','A','B','A'])
        decrement( ['B','A','B'] ) = ['B','B','A']

        if it cannot be decremented, return the arg itself.
        """
        A_found = False
        for k in range( len(char_array) ):
            if A_found == False and  char_array[k] == 'A':
                A_found = True
            elif A_found == True and char_array[k] == 'B':
                char_array[k-1] = 'B'
                char_array[k] = 'A'
                return char_array

        return char_array

    def createString(self, N, K):
        max_val = self.max_value( N )
        if K > max_val:
            return ""
        
        char_array = self.max_value_chars( N )
        # repeat the decrement until the value gets to K
        for k in range( max_val - K ):
            char_array = self.decrement( char_array )
            
        return "".join( char_array )

if __name__ == "__main__":
    print AB().createString(50, 201)
