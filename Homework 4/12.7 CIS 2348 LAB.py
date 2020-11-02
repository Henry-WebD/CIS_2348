#Henry Saravia, PSID: 1853318

def get_age():
    user_age = int(input())
    if 18 <= user_age <= 75:
        return user_age
    raise ValueError("Invalid age.")


def fat_burning_heart_rate(user_age):
    return (220 - user_age) * 0.7


if __name__ == "__main__":
    try:
        user_age = get_age()
        print("Fat burning heart rate for a " + str(user_age) + " year-old: " + str(fat_burning_heart_rate(user_age)) + " bpm")
    except ValueError as e:
        print(e)
        print("Could not calculate heart rate info.")
        print()
