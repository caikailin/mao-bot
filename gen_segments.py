import json

segments = []

s1 = {
    "id": 1, "work": "《实践论》", "title": "实践是认识的来源和基础",
    "original": "马克思主义者认为人类的生产活动是最基本的实践活动，它决定其他一切活动。……马克思主义者认为，只有人们的社会实践，才是人们对于外界认识的真理性的标准。……你要知道梨子的滋味，你就得变革梨子，亲口吃一吃。",
    "insight": "【观点提点】毛泽东开宗明义指出：实践是第一位的，认识来源于实践，并且必须回到实践中去检验。这就是「实践第一」的观点。",
    "example": "【举例说明】就像学游泳，光看游泳教程（理论）不下水（实践），永远学不会；只有跳进水里扑腾，咃几口水，才能真正掌握游泳技能。工作中的新方案、新产品，都需要在实践中验证和完善。"
}

segments.append(s1)

# Actually, let me just write segments directly from the Python file approach
# This unicode escaping approach is too tedious

print("Will write segments differently")
