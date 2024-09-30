from flask import Flask, request, jsonify
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


def binary_search_videos(videos, target_title):
    
    left, right = 0, len(videos) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        mid_title = videos[mid]

        if mid_title == target_title:
            return mid  
        elif mid_title < target_title:
            left = mid + 1  
        else:
            right = mid - 1

    return -1  


@app.route('/search', methods=['GET'])
def search_videos():
    query = request.args.get('query')
    
    if not query:
        return jsonify({"error": " 'query' is required."}), 400

    index = binary_search_videos(video_titles, query)
    
    if index != -1:
        return jsonify({"title": video_titles[index], "index": index}), 200
    else:
        return jsonify({"message": "Video not found."}), 404

if __name__ == '__main__':
    app.run(debug=True)