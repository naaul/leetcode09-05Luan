

def maximumHappinessSum(happiness, k):
        happiness.sort(reverse= True)

        i = 0
        sum = 0
        while k > 0:
              if happiness[0 + i] - i < 0:
                    sum += 0
              else:
                sum += happiness[0 + i] - i
              i += 1
              k -= 1

        return sum
              


happiness = [12,1,42]

k = 3

maximumHappinessSum(happiness, k)