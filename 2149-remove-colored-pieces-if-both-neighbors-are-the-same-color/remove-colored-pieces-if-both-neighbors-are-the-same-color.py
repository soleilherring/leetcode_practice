class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        # colors = "A AX A B A B B" true 
        #   "A B B B B B B B A A A"        
        #                x      x

        # get the count for each person
        alice_count = 0
        bob_count = 0

        # start at 1 because checking the element before and after it
        # so [A A B A A A] -> would start at A at 1 positon and check the before and after elemnts
        for i in range(1, len(colors)-1): #only go to len(str) -1 because would stop at the second to last element because it's teh last one to have an element after it

            if colors[i-1] == colors[i] == colors[i + 1]:
                if colors[i] == 'A':
                    alice_count +=1 
                if colors[i] == 'B':
                    bob_count +=1
        # if there is a tie, bob wins we ONLY want alice to win if she has a higher count
        # bob wins otherwise
        return alice_count > bob_count 