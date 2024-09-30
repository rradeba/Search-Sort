from flask import Flask, jsonify

app = Flask(__name__)

video_titles = [
    "The Art of Coding",
    "Exploring the Cosmos",
    "Cooking Masterclass: Italian Cuisine",
    "History Uncovered: Ancient Civilizations",
    "Fitness Fundamentals: Strength Training",
    "Digital Photography Essentials",
    "Financial Planning for Beginners",
    "Nature's Wonders: National Geographic",
    "Artificial Intelligence Revolution",
    "Travel Diaries: Discovering Europe"
]



def merge_sort(titles):
    
    if len(titles) <= 1:
        return titles

    
    mid = len(titles) // 2
    left_half = merge_sort(titles[:mid]) 
    right_half = merge_sort(titles[mid:])  

  
    return merge(left_half, right_half)

def merge(left, right):
    sorted_titles = []
    left_index, right_index = 0, 0

    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_titles.append(left[left_index])
            left_index += 1
        else:
            sorted_titles.append(right[right_index])
            right_index += 1

  
    while left_index < len(left):
        sorted_titles.append(left[left_index])
        left_index += 1

    
    while right_index < len(right):
        sorted_titles.append(right[right_index])
        right_index += 1

    return sorted_titles




@app.route('/videos/sorted', methods=['GET'])
def get_sorted_videos():
    sorted_titles = merge_sort(video_titles)
    return jsonify({"sorted_videos": sorted_titles}), 200

if __name__ == '__main__':
    app.run(debug=True)
