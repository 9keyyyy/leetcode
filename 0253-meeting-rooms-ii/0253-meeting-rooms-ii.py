class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
    
        # 모든 시작 시간과 종료 시간을 분리해서 저장
        events = []
        
        for start, end in intervals:
            events.append((start, 'start'))  # 회의 시작
            events.append((end, 'end'))      # 회의 종료
        
        # 시간 순으로 정렬
        # 같은 시간이면 종료를 먼저 처리 (end가 start보다 사전순으로 앞서므로)
        events.sort()
        
        current_meetings = 0  # 현재 진행 중인 회의 개수
        max_rooms = 0         # 필요한 최대 회의실 개수
        
        for time, event_type in events:
            if event_type == 'start':
                current_meetings += 1  # 회의 시작 -> 회의실 하나 더 필요
                max_rooms = max(max_rooms, current_meetings)
            else:  # event_type == 'end'
                current_meetings -= 1  # 회의 종료 -> 회의실 하나 반납
        
        return max_rooms