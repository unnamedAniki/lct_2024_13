import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import classification_report

# Загрузка данных
file_path = 'ЛЦТ.xlsx'
df = pd.read_excel(file_path)

df.fillna({
    'gender': df['gender'].mode()[0],
    'age': df['age'].mean(),
    'reg_region_nm': 'Unknown',
    'cnt_tr_all_3m': 0,
    'cnt_tr_top_up_3m': 0,
    'cnt_tr_cash_3m': 0,
    'cnt_tr_buy_3m': 0,
    'cnt_tr_mobile_3m': 0,
    'cnt_tr_oil_3m': 0,
    'cnt_tr_on_card_3m': 0,
    'cnt_loans': 0,
    'cnt_deposits': 0,
    'avg_outstanding_amount_3m': 0,
    'cnt_dep_act': 0,
    'sum_dep_now': 0,
    'avg_dep_avg_balance_1month': 0,
    'max_dep_avg_balance_3month': 0,
    'app_vehicle_ind': 0,
    'app_position_type_nm': 'Unknown',
    'visit_purposes': 'Unknown',
    'qnt_months_from_last_visit': df['qnt_months_from_last_visit'].mean(),
    'super_clust': 'Unknown'
}, inplace=True)

# Предварительная обработка данных
df.fillna(0, inplace=True)

# Кодирование категориальных переменных
label_encoders = {}
categorical_columns = ['reg_region_nm', 'app_position_type_nm', 'super_clust', 'visit_purposes']

for column in categorical_columns:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column].astype(str))
    label_encoders[column] = le

# Масштабирование числовых переменных
scaler = StandardScaler()
numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
df[numeric_columns] = scaler.fit_transform(df[numeric_columns])

# Разделение данных на признаки и целевые метки
X = df.drop(columns=['super_clust'])
y = df['super_clust']

# Разделение на тренировочные и тестовые данные
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Обучение модели Random Forest
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)

# Оценка модели
y_pred = rf_model.predict(X_test)
print("Random Forest Classification Report:")
print(classification_report(y_test, y_pred))

# Обучение модели Gradient Boosting
gb_model = GradientBoostingClassifier(random_state=42)
gb_model.fit(X_train, y_train)

# Оценка модели
y_pred_gb = gb_model.predict(X_test)
print("Gradient Boosting Classification Report:")
print(classification_report(y_test, y_pred_gb))

# Кросс-валидация и тюнинг гиперпараметров для Random Forest
param_grid = {
    'n_estimators': [100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5],
    'min_samples_leaf': [1, 2],
}

grid_search_rf = GridSearchCV(estimator=rf_model, param_grid=param_grid, cv=5, n_jobs=-1, verbose=2)
grid_search_rf.fit(X_train, y_train)

print("Best parameters for Random Forest:", grid_search_rf.best_params_)

# Кросс-валидация и тюнинг гиперпараметров для Gradient Boosting
param_grid_gb = {
    'n_estimators': [100, 200],
    'learning_rate': [0.01, 0.1],
    'max_depth': [3, 5],
    'subsample': [0.8, 1.0],
}

grid_search_gb = GridSearchCV(estimator=gb_model, param_grid=param_grid_gb, cv=5, n_jobs=-1, verbose=2)
grid_search_gb.fit(X_train, y_train)

print("Best parameters for Gradient Boosting:", grid_search_gb.best_params_)

# Обучение моделей с лучшими параметрами
best_rf_model = grid_search_rf.best_estimator_
best_gb_model = grid_search_gb.best_estimator_

# Оценка лучших моделей
y_pred_best_rf = best_rf_model.predict(X_test)
print("Best Random Forest Classification Report:")
print(classification_report(y_test, y_pred_best_rf))

y_pred_best_gb = best_gb_model.predict(X_test)
print("Best Gradient Boosting Classification Report:")
print(classification_report(y_test, y_pred_best_gb))


# Функция для рекомендаций на основе правил и модели
def recommend_service(user_data):
    recommendations = []

    # Применение бизнес-логики
    if user_data['cnt_tr_all_3m'] > 50:
        recommendations.append('Кредитная карта')
    if user_data['avg_dep_avg_balance_1month'] > 500:
        recommendations.append('Депозит')
    if user_data['cnt_tr_mobile_3m'] > 5:
        recommendations.append('Премиальная карта')
    if user_data['cnt_dep_act'] > 1:
        recommendations.append('Накопительный счет')
    if user_data['cnt_tr_cash_3m'] > 10:
        recommendations.append('Кредит под залог недвижимости')
    if user_data['cnt_tr_oil_3m'] > 10:
        recommendations.append('Кредит под залог авто')
    if user_data['app_vehicle_ind'] == 1:
        recommendations.append('Классический автокредит')

    # Применение моделей машинного обучения
    user_df = pd.DataFrame([user_data])
    for column in categorical_columns:
        user_df[column] = label_encoders[column].transform(user_df[column].astype(str))
    user_df[numeric_columns] = scaler.transform(user_df[numeric_columns])

    predicted_super_clust_rf = best_rf_model.predict(user_df.drop(columns=['super_clust']))
    predicted_service_rf = label_encoders['super_clust'].inverse_transform(predicted_super_clust_rf)

    predicted_super_clust_gb = best_gb_model.predict(user_df.drop(columns=['super_clust']))
    predicted_service_gb = label_encoders['super_clust'].inverse_transform(predicted_super_clust_gb)

    recommendations.append(predicted_service_rf[0])
    recommendations.append(predicted_service_gb[0])

    return recommendations


# Пример использования функции для рекомендаций
example_user = df.iloc[0].to_dict()
recommended_services = recommend_service(example_user)
print("Recommended services:", recommended_services)
