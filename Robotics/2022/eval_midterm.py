import inspect
import copy
import pandas as pd
from glob import glob
import importlib

import midterm_correct_answer as cor_ans
import executers

DST_PATH = "C:/Users/SCH/Desktop"


def evaluate_main():
    set_print_options()
    score_table = pd.DataFrame()
    module_list = glob("./renamed/*.py")
    module_list = [mod.strip("./").strip(".py").replace("\\", ".") for mod in module_list]
    print("submitted module list:", module_list)

    exec_classes = [cls_type for name, cls_type in inspect.getmembers(executers) if inspect.isclass(cls_type)]
    exec_classes.remove(executers.ExecTemplate)
    print("evaluation class list:", exec_classes)
    
    for module in module_list:
        print("\n\n" + "#"*30 + "\n" + "MODULE:", module)
        try:
            sub_ans = importlib.import_module(module)
        except Exception as e:
            print("[import error]", e)
            continue

        indiv_scores = {}
        for cls_type in exec_classes:
            print("~"*10, "Test", cls_type.__name__, "~"*10)
            cor_exc, sub_exc = cls_type(cor_ans), cls_type(sub_ans)
            indiv_scores[cor_exc.target_name] = evaluate_problem(cor_exc, sub_exc)

        indiv_scores["total"] = sum(list(indiv_scores.values()))
        indiv_scores["name"] = module.split(".")[1]
        # score_table = score_table.append(indiv_scores, ignore_index=True)
        score_table = pd.concat([score_table, pd.DataFrame.from_records([indiv_scores])])
        print("score table\n", score_table)

    print("="*30)
    print("score_table:", score_table)
    # score_table.to_csv(os.path.join(DST_PATH, "systprog_eval.csv"), index=False)


def set_print_options():
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)
    pd.set_option('display.colheader_justify', 'center')
    pd.set_option('display.precision', 3)


def evaluate_problem(cor_exc, sub_exc):
    expected = copy.deepcopy(cor_exc.run())
    result = copy.deepcopy(sub_exc.run())

    score_sum = 0
    for test_key in cor_exc.scores:
        if test_key in result and expected[test_key] == result[test_key]:
            score_sum += cor_exc.scores[test_key]
            print(f"  {cor_exc.target_name}/{test_key} scored {cor_exc.scores[test_key]}")
        else:
            print(f">>{cor_exc.target_name}/{test_key} FAILED")
            if test_key in result:
                print(f"\tcompare: /{expected[test_key]}/{result[test_key]}/")
    print(f"{cor_exc.target_name} scored {score_sum}")
    return score_sum


if __name__ == "__main__":
    evaluate_main()
