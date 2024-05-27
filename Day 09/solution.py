def main():
    with open("input.txt") as f:
        report = f.read().splitlines()
    
    solution(report, 1)
    solution(report, 2)


def solution(report, stage):
    predictions = []
    for history in report:
        parsed_history = parse_history(history)
        if stage == 2:
            parsed_history = parsed_history[::-1] # Fastest way to reverse a list apparently
        predictions.append(get_extrapolation(parsed_history))
    
    print(f"Solution {stage}: {sum(predictions)}")


def get_extrapolation(series):
    if len(set(series)) == 1:
        return series[0]
    
    difference_series = []
    for index, value in enumerate(series[1:]):
        difference_series.append(value-series[index])
    
    return series[-1] + get_extrapolation(difference_series)


def parse_history(history_string):
    return [int(x) for x in history_string.split()]


if __name__ == "__main__":
    main()
