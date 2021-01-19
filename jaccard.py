import itertools

### CREATE A FUNCTION FOR JACCARD SIMILARITY WITH TWO OBJECTS
def jaccard(first, second):
  union_set = first.union(second)
  inter_set = first.intersection(second)

  len_union = len(union_set)
  len_inter = len(inter_set)

  sim_score = len_inter*1.0 / len_union*1.0

  print(sim_score)

### CREATE VARIABLES TO STORE THE OBJECTS
cohorts = {
  "all-traffic": {'top-100-prospects-rankings-midseason-update-story', 'dustin-may-aj-pollock-propel-dodgers-story', 'cubs-hold-off-royals-for-fifth-straight-victory-story', 'albert-pujols-willie-mays-home-run-chase-story', 'yankees-homer-in-first-11-games-of-2020-story'},
  "external-traffic": {'top-100-prospects-rankings-midseason-update-story', 'melanie-newman-makes-history-calling-orioles-on-radio-story', 'mlb-top-100-prospects-list-for-2020-story', 'albert-pujols-willie-mays-home-run-chase-story', 'cubs-hold-off-royals-for-fifth-straight-victory-story'},
  "external-boomer": {'top-100-prospects-rankings-midseason-update-story', 'cubs-hold-off-royals-for-fifth-straight-victory-story', 'melanie-newman-makes-history-calling-orioles-on-radio-story', 'six-cardinals-positive-covid-19-tests-story', 'lucas-giolito-helps-white-sox-extend-winning-streak-story'},
  "external-gen-x": {'top-100-prospects-rankings-midseason-update-story', 'melanie-newman-makes-history-calling-orioles-on-radio-story', 'cubs-hold-off-royals-for-fifth-straight-victory-story', 'mlb-announces-expanded-playoffs-for-2020-story', 'dustin-may-aj-pollock-propel-dodgers-story'},
  "external-mill": {'top-100-prospects-rankings-midseason-update-story', 'mlb-top-100-prospects-list-for-2020-story', 'mlb-announces-expanded-playoffs-for-2020-story', 'jake-diekman-chaz-roe-slider-pitching-ninja-story', 'melanie-newman-makes-history-calling-orioles-on-radio-story'},
  "all-boomer": {'top-100-prospects-rankings-midseason-update-story', 'dustin-may-aj-pollock-propel-dodgers-story', 'cubs-hold-off-royals-for-fifth-straight-victory-story', 'cardinals-cleared-to-end-quarantine-story', 'max-scherzer-exits-with-injury-vs-mets-story'},
  "all-gen-x": {'top-100-prospects-rankings-midseason-update-story', 'dustin-may-aj-pollock-propel-dodgers-story', 'cubs-hold-off-royals-for-fifth-straight-victory-story', 'max-scherzer-exits-with-injury-vs-mets-story', 'cardinals-cleared-to-end-quarantine-story'},
  "all-mill": {'top-100-prospects-rankings-midseason-update-story', 'dustin-may-aj-pollock-propel-dodgers-story', 'max-scherzer-exits-with-injury-vs-mets-story', 'albert-pujols-willie-mays-home-run-chase-story', 'cubs-hold-off-royals-for-fifth-straight-victory-story'},
  "boomer-male": {'top-100-prospects-rankings-midseason-update-story','dustin-may-aj-pollock-propel-dodgers-story','cubs-hold-off-royals-for-fifth-straight-victory-story','cardinals-cleared-to-end-quarantine-story','albert-pujols-willie-mays-home-run-chase-story'},
  "boomer-female": {'top-100-prospects-rankings-midseason-update-story','dustin-may-aj-pollock-propel-dodgers-story','cubs-hold-off-royals-for-fifth-straight-victory-story','six-cardinals-positive-covid-19-tests-story','cardinals-cleared-to-end-quarantine-story'},
  "gen-x-male": {'top-100-prospects-rankings-midseason-update-story','dustin-may-aj-pollock-propel-dodgers-story','cubs-hold-off-royals-for-fifth-straight-victory-story','max-scherzer-exits-with-injury-vs-mets-story','cardinals-cleared-to-end-quarantine-story'},
  "gen-x-female": {'top-100-prospects-rankings-midseason-update-story','dustin-may-aj-pollock-propel-dodgers-story','cubs-hold-off-royals-for-fifth-straight-victory-story','cardinals-cleared-to-end-quarantine-story','max-scherzer-exits-with-injury-vs-mets-story'},
  "mill-male": {'top-100-prospects-rankings-midseason-update-story','dustin-may-aj-pollock-propel-dodgers-story','albert-pujols-willie-mays-home-run-chase-story','max-scherzer-exits-with-injury-vs-mets-story','cardinals-cleared-to-end-quarantine-story'},
  "mill-female": {'top-100-prospects-rankings-midseason-update-story','dustin-may-aj-pollock-propel-dodgers-story'},
  "BOS": {'top-100-prospects-rankings-midseason-update-story', 'dustin-may-aj-pollock-propel-dodgers-story', 'red-sox-losing-streak-at-four-games-story', 'josh-taylor-darwinzon-hernandez-closer-joining-red-sox-story', 'albert-pujols-willie-mays-home-run-chase-story'},
  "DET": {'top-100-prospects-rankings-midseason-update-story', 'tigers-farm-system-strong-in-new-rankings-story', 'dustin-may-aj-pollock-propel-dodgers-story', 'max-scherzer-exits-with-injury-vs-mets-story', 'tigers-making-most-of-unexpected-time-off-story'},
  "LAA": {'top-100-prospects-rankings-midseason-update-story', 'dustin-may-aj-pollock-propel-dodgers-story', 'albert-pujols-willie-mays-home-run-chase-story', 'shohei-ohtani-done-pitching-in-2020-story', 'jo-adell-called-up-by-angels-story'},
  "PIT": {'top-100-prospects-rankings-midseason-update-story', 'pirates-losing-streak-continues-vs-twins-story', 'nick-burdi-elbow-injury-2020-season-over-story', 'dustin-may-aj-pollock-propel-dodgers-story', 'derek-shelton-pranked-by-friend-rocco-baldelli-story'},
  "CHC": {'cubs-hold-off-royals-for-fifth-straight-victory-story', 'top-100-prospects-rankings-midseason-update-story', 'kris-bryant-keeps-homer-promise-to-infant-son-story', 'dustin-may-aj-pollock-propel-dodgers-story', 'david-ross-maintains-trust-in-craig-kimbrel-story'},
  "ATL": {'top-100-prospects-rankings-midseason-update-story', 'matt-adams-left-hamstring-tightness-story', 'braves-options-with-mike-soroka-injured-story', 'max-fried-braves-defeat-blue-jays-story', 'dustin-may-aj-pollock-propel-dodgers-story'
  }
}

cohorts = {
  "all-traffic": {'top-100-prospects-rankings-midseason-update-story', 'dustin-may-aj-pollock-propel-dodgers-story', 'cubs-hold-off-royals-for-fifth-straight-victory-story', 'albert-pujols-willie-mays-home-run-chase-story', 'yankees-homer-in-first-11-games-of-2020-story'},
  "veteran": {'top-100-prospects-rankings-midseason-update-story', 'dustin-may-aj-pollock-propel-dodgers-story', 'max-scherzer-exits-with-injury-vs-mets-story', 'cardinals-cleared-to-end-quarantine-story', 'albert-pujols-willie-mays-home-run-chase-story'},
  "rookie": {'top-100-prospects-rankings-midseason-update-story', 'dustin-may-aj-pollock-propel-dodgers-story', 'cubs-hold-off-royals-for-fifth-straight-victory-story', 'albert-pujols-willie-mays-home-run-chase-story', 'cardinals-cleared-to-end-quarantine-story'},
  "team": {'top-100-prospects-rankings-midseason-update-story', 'dustin-may-aj-pollock-propel-dodgers-story', 'cubs-hold-off-royals-for-fifth-straight-victory-story', 'cardinals-cleared-to-end-quarantine-story', 'max-scherzer-exits-with-injury-vs-mets-story'},
  "medium-80": {'top-100-prospects-rankings-midseason-update-story', 'dustin-may-aj-pollock-propel-dodgers-story', 'cubs-hold-off-royals-for-fifth-straight-victory-story', 'albert-pujols-willie-mays-home-run-chase-story', 'shohei-ohtani-done-pitching-in-2020-story'},
  "light-50": {'top-100-prospects-rankings-midseason-update-story', 'dustin-may-aj-pollock-propel-dodgers-story', 'albert-pujols-willie-mays-home-run-chase-story', 'cubs-hold-off-royals-for-fifth-straight-victory-story', 'lucas-giolito-helps-white-sox-extend-winning-streak-story'},
  "power-95": {'top-100-prospects-rankings-midseason-update-story', 'dustin-may-aj-pollock-propel-dodgers-story', 'cubs-hold-off-royals-for-fifth-straight-victory-story', 'cardinals-cleared-to-end-quarantine-story', 'max-scherzer-exits-with-injury-vs-mets-story'}
  }

cohorts = {
  'all-traffic': {'top-100-prospects-rankings-midseason-update-story', 'dustin-may-aj-pollock-propel-dodgers-story', 'cubs-hold-off-royals-for-fifth-straight-victory-story', 'albert-pujols-willie-mays-home-run-chase-story', 'yankees-homer-in-first-11-games-of-2020-story'},
  'all-male': {'top-100-prospects-rankings-midseason-update-story', 'dustin-may-aj-pollock-propel-dodgers-story', 'cubs-hold-off-royals-for-fifth-straight-victory-story', 'cardinals-cleared-to-end-quarantine-story', 'albert-pujols-willie-mays-home-run-chase-story'},
  'all-female': {'top-100-prospects-rankings-midseason-update-story', 'dustin-may-aj-pollock-propel-dodgers-story', 'cubs-hold-off-royals-for-fifth-straight-victory-story', 'cardinals-cleared-to-end-quarantine-story', 'six-cardinals-positive-covid-19-tests-story'},
  'external-female': {'top-100-prospects-rankings-midseason-update-story', 'dustin-may-aj-pollock-propel-dodgers-story', 'melanie-newman-makes-history-calling-orioles-on-radio-story', 'juan-soto-dances-on-top-of-dugout-story', 'cubs-hold-off-royals-for-fifth-straight-victory-story'},
  'external-male': {'top-100-prospects-rankings-midseason-update-story', 'mlb-top-100-prospects-list-for-2020-story', 'cubs-hold-off-royals-for-fifth-straight-victory-story', 'melanie-newman-makes-history-calling-orioles-on-radio-story', 'mlb-announces-expanded-playoffs-for-2020-story'}
}

# ITERATE through the key combos
combos = list(itertools.combinations(cohorts, 2))
len_combos = len(combos)

for i in range(len_combos):
  #global combos
  #global cohorts
  x, y = combos[i]
  print(x, y)
  jaccard(cohorts[x], cohorts[y])
