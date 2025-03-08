///https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

struct TrieNode {
    TrieNode *children[2];
    TrieNode() {
        children[0] = children[1] = nullptr;
    }
};

class Solution {
private:
    TrieNode *root;

    void insert(int k) {
        TrieNode *now = root;
        for (int i = 30; i >= 0; i--) {
            int bit = (k & (1<<i)) >> i;
            if (!now->children[bit]) now->children[bit] = new TrieNode();
            now = now->children[bit];
        }
    }

public:
    Solution() {
        root = new TrieNode();
    }

    int findMaximumXOR(vector<int> &v) {
        for (int k: v) insert(k);

        int ans = 0;
        for (int k: v) {
            int want = INT_MAX ^ k; ///the perfect pair for k.
            TrieNode *now = root;

            ///suppose all numbers but one have the MSB different from want's MSB.
            ///we prefer the number with the same MSB as want, even if it may be different on all other positions from want.
            ///the sum of the contributions of the other bits is strictly smaller than what we can gain from the matched MSB.
            ///greedy: pick the subset of numbers that share want's MSB. from that subset, pick again against want's next MSB, ...

            for (int i = 30; i >= 0; i--) {
                int bit = (want & (1<<i)) >> i;
                if (now->children[bit]) { ///from the remaining numbers, at least one of them has the preferred bit for want.
                    now = now->children[bit];
                } else { ///am obligated to choose the other value for the bit.
                    now = now->children[bit ^ 1];
                    want ^= (1<<i);
                }
            }

            ans = std::max(ans, k ^ want);
        }

        return ans;
    }
};
