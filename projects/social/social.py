import random


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """

        # ? Stretch:
        # If numbers of users is too high, averages and percentages become unrealistic
        # Tricky part is finding what the cap is.

        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Add users
        for i in range(num_users):
            self.add_user(f"User {i+1}")

        # Create friendships
        """
        Hint 1: To create N random friendships, you could create a list with 
        all possible friendship combinations, shuffle 
        the list, then grab the first N elements from the list. 
        You will need to import random to get shuffle.
        """
        # total_friendships = avg_friendships * num_users

        # Create a list with all possible friendship combos
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id+1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        # shuffle the list (uses Fisher-Yates O(N) shuffle)
        random.shuffle(possible_friendships)

        # grab the first N elements from the list
        # of times to call add_friendship = avg_friendships * num_users / 2
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """

        # BFT -- for each connected friend, check to see if friend already in visited
        # if not, create a key-value pair in visited with friend value as key, path to friend as value

        visited = {}  # Note that this is a dictionary, not a set

        # Create an empty queue and enqueue the starting [path]
        q = Queue()
        q.enqueue([user_id])  # [1] and not 1
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first path
            path = q.dequeue()

            # If the last friend in the path has not been visited...
            last_friend = path[-1]

            if last_friend not in visited:
                # Mark it as visited
                visited[last_friend] = path

                neighbors = self.friendships[last_friend]
                for neighbor in neighbors:
                    copy = path.copy()
                    copy.append(neighbor)
                    q.enqueue(copy)

        return visited

    def average_percentage_of_connections(self):
        """
        Returns the average percentage of the total user population that is in each user's
        extended social network
        """
        total_percentage = 0
        for user in self.users:
            connections = len(self.get_all_social_paths(user))-1
            if connections > 0:
                user_percentage = connections / (len(self.users)-1)
                total_percentage += user_percentage
        return total_percentage / len(self.users) * 100

    def degree_of_separation(self, user):
        degree_total = 0
        connections = self.get_all_social_paths(user)
        for conn in connections:
            degree_total += len(connections[conn])-1
        return degree_total / len(connections)-1

    def average_degree_of_separation(self):
        """
        Returns the averaged average degree of separation for all 
        users within their specific network
        """
        total_averages = 0
        for user in self.users:
            total_averages += self.degree_of_separation(user)
        return total_averages / len(self.users)


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(1000, 5)
    # print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    # print(f"\n{connections}")
    total_connections = sg.average_percentage_of_connections()
    print(f"\n{total_connections}")
    avg_degrees = sg.average_degree_of_separation()
    print(f"{avg_degrees}")
