class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        str_to_list = {} 
        
        for s in strs:
            key = ''.join(sorted(s))
            print(key)

            if key not in str_to_list:
                str_to_list[key] = []
            str_to_list[key].append(s)
        
        return list(str_to_list.values())
       