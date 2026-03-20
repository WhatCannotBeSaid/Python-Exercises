name=['A', 'B', 'C', 'D', 'E']
print(f"尊敬的{name[0]},我邀请你参加晚宴。")
print(f"尊敬的{name[2]},我邀请你参加晚宴。")
print(f"尊敬的{name[4]},我邀请你参加晚宴。")
print(f"很抱歉，{name[2]}不能参加晚宴。")
del name[2]
name.append('F')
print(f"尊敬的{name[0]},我邀请你参加晚宴。")
print(f"尊敬的{name[3]},我邀请你参加晚宴。")
print(f"尊敬的{name[4]},我邀请你参加晚宴。")