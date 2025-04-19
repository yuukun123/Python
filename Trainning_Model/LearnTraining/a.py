# khai báo thư viện cần thiết cho việc tạo mô hình và đánh giá hiệu quả của từng mô hình
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score, RandomizedSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from scipy import stats
import joblib  # Import joblib for saving and loading models


# Function to load data with error handling for encoding
# khởi tạo hàm để đọc dữ liệu từ file data có đuôi là csv
def load_data(file_path):
    encodings = ['utf-8', 'latin1', 'ISO-8859-1']  # List of common encodings
    for enc in encodings:
        try:
            # mở file csv để đọc 
            df = pd.read_csv(file_path, encoding=enc)
            # thông báo đã mở file thành công
            print(f"Data loaded successfully with encoding: {enc}")
            # trả về dữ liệu file
            return df
        # 
        except UnicodeDecodeError:
            # thông báo việc đọc file thất bại
            print(f"Failed to decode with encoding: {enc}")
            # trả về thông báo không thể mở file
    raise ValueError("Unable to load data with provided encodings.")

# Function to explore the data
# khởi tạo hàm để đọc tát cả dữ liệu trong file
def explore_data(df):
    # thống kê dữ liệu và hiện dữ liệu đã tóm tắt 
    print(df.describe())
    # hiện nhứng thông tin của dữ liệu 
    print(df.info())
    
    # vẽ biểu đồ để thể hiện tính trực quan và phân bố trong dữ liệu
    numeric_features = df.select_dtypes(include=['float64', 'int64']).columns
    for feature in numeric_features:
        sns.histplot(df[feature])
        # tiêu đề của biểu đồ
        plt.title(f'Distribution of {feature}')
        # hiện biểu đồ đã vẽ lên mafn hình
        plt.show()
    
    # vẽ biểu đồ ma trận nhiệt để thể hiện tính tương quan giữa dữ liệu số
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
    # tiêu đề của biểu đồ ma trận
    plt.title('Correlation Matrix')
    # hiện biểu đồ đã vẽ lên mafn hình
    plt.show()

# Function to preprocess the data and generate a synthetic target
# Mục đích: Xử lý trước dữ liệu bằng cách xử lý các giá trị bị thiếu, giá trị ngoại lệ và mã hóa các tính năng phân loại.
def preprocess_data(df):
    # Handle missing values
    #sử lý những giá trị bị thiếu trong dữ liệu bằng cách tính giá trị trung bình cho các cột số
    df.fillna(df.mean(numeric_only=True), inplace=True)
    
    # Handle outliers
    # xử lý các giá trị ngoại lệ bằng cách xóa các hàng có điểm z nào lớn hơn 3
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    z_scores = np.abs(stats.zscore(numeric_df))
    df = df[(z_scores < 3).all(axis=1)]
    
    # Add synthetic target column (e.g., random values)
    # thêm cột mục tiêu giả lập bằng cách thêm các giá trị ngẫu nhiên
    df['SyntheticTarget'] = np.random.rand(len(df)) * 100  # Example synthetic target
    
    # Encode categorical features
    # mã hóa các biến bằng cách chuyển đổi các cột phân loại thành các biến giả
    df = pd.get_dummies(df)
    
    # Split the dataset into training and testing sets
    # chia dữ liệu thành tập huấn luyện và tập kiểm tra
    X = df.drop('SyntheticTarget', axis=1)
    y = df['SyntheticTarget']
    
    # trả về các giá trị huấn luyện
    return df, train_test_split(X, y, test_size=0.2, random_state=42)

# Function to train and evaluate models
# đào tạo các mô hình khác nhau, đánh giá hiệu suất hoạt động và lưu mô hình tối ưu nhất vào file
def train_and_evaluate_models(X_train, X_test, y_train, y_test):
    # 4 loại mô hình cần đào tạo
    models = {
        'Linear Regression': LinearRegression(),
        'Decision Tree': DecisionTreeRegressor(),
        'Random Forest': RandomForestRegressor(),
        'SVM': SVR()
    }
    
    # đào tạo và đánh giá hiệu suất hoạt động của các mô hình
    #khởi tạo biến mô hình tốt nhất
    best_model_name = None
    # khởi tạo biến điểm của mô hinh tốt nhất là âm vô cùng
    best_model_score = -np.inf  # Initialize to negative infinity
    # khởi tạo biến hiệu suất để lưu các số liệu đánh giá cho từng mô hinhf
    performance_metrics = {}

    for name, model in models.items():
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        
        # Save the model
        #lưu từng mô hình vào file riêng 
        joblib.dump(model, f'{name.replace(" ", "_")}_model.pkl')
        print(f"Saved {name} model to {name.replace(' ', '_')}_model.pkl")
        
        # khởi tạo các điểm để đánh giá mô hình
        r2 = r2_score(y_test, predictions)
        rmse = mean_squared_error(y_test, predictions, squared=False)
        mae = mean_absolute_error(y_test, predictions)
        cv_scores = cross_val_score(model, X_train, y_train, cv=5)
        
        # các điểm để đánh giá hiệu suất mô hình
        performance_metrics[name] = {
            'R²': r2,
            'RMSE': rmse,
            'MAE': mae,
            'CV Score': cv_scores.mean()
        }
        
        # hiện ra điểm đánh giá của từng mô hình
        print(f"{name} - Train Score: {model.score(X_train, y_train)}")
        print(f"{name} - R²: {r2}")
        print(f"{name} - RMSE: {rmse}")
        print(f"{name} - MAE: {mae}")
        print(f"{name} - CV Scores: {cv_scores.mean()}\n")
        
        
        # Update best model if necessary
        #  nếu điểm đánh giá của mô hình này cao hơn điểm đánh giá của mô hình tối ưu hiện tại
        # xác định mô hình tốt nhất dựa trên điểm r2
        if r2 > best_model_score:  # or use another criterion
            best_model_score = r2
            best_model_name = name

    # hiện ra tên moo hình có điểm r2 tốt nhất
    print(f"The best model based on R² score is: {best_model_name}")
    return performance_metrics

# Function to perform hyperparameter tuning
# thực hiện điều chỉnh siêu tham số trên mô hình
def hyperparameter_tuning(X_train, y_train):
    # xác định tham số bằng cách chỉ định phạm vi siêu tham số để điều chỉnh
    param_distributions = {
        'n_estimators': [10, 50, 100],
        'max_depth': [None, 10, 20],
    }
    
    # biến random để tìm ra các tham số tốt nhất
    random_search = RandomizedSearchCV(RandomForestRegressor(), param_distributions, n_iter=10, cv=5, random_state=42)
    random_search.fit(X_train, y_train)
    
    # lưu mô hình tốt nhất trong quá trình tìm kiếm vào file có đuôi pkl 
    joblib.dump(random_search.best_estimator_, 'Best_RandomForest_Model.pkl')
    # hiện ra thông báo đã lưu mô hình tốt nhất trong quá trinh tìm kiếm ngẫu nhiên
    print(f"Saved best RandomForest model to Best_RandomForest_Model.pkl")
    #  hiện ra thông tin về mô hình tốt nhất
    print(f"Best Parameters: {random_search.best_params_}")
    
    # trả về mô hình tốt nhất
    return random_search.best_estimator_

# Function to test the best model
# kiểm tra mô hình tốt nhất và đánh giá hiệu suất của nó
def test_best_model(X_test, y_test, model):
    # sử dụng mô hình tốt nhất để dự đoán
    test_predictions = model.predict(X_test)
    # hiện ra những đánh giá và các thông số cho mô hình tốt nhất
    print(f"Best Model R²: {r2_score(y_test, test_predictions)}")
    print(f"Best Model RMSE: {mean_squared_error(y_test, test_predictions, squared=False)}")
    print(f"Best Model MAE: {mean_absolute_error(y_test, test_predictions)}")

# Function to perform K-Means clustering and visualize results
# thực hiện phân cụm va trực quan hóa kết quả
def clustering_analysis(df):
    # Prepare data for clustering
    # chuẩn bị dữ liệu cho phân cụm
    # định nghĩa hàm và lấy data frame df làm đối số và thực hiện phân cụm dữ liệu
    
    # dòng này chỉ chọn các cột số từ data frame và lưu trữ chúng trong numeric_df
    numeric_df = df.select_dtypes(include=['float64', 'int64'])  # Ensure using only numeric columns
    # tạo bản sao và lưu trữ chúng trong X và sẽ không ảnh hướng đến dữ liệu gốc
    X = numeric_df.copy()
    
    # khởi tạo đối tượng StandardScaler từ mô-đun sklearn.preprocessing. 
    # StandardScaler được sử dụng để chuẩn hóa các tính năng bằng cách loại bỏ giá trị trung bình và tỷ lệ theo phương sai đơn vị.
    """
    Điều này quan trọng đối với các thuật toán phân cụm 
    vì nó đảm bảo rằng mỗi tính năng đều đóng góp như nhau vào các phép tính khoảng cách
    """
    scaler = StandardScaler()
    # Dòng này áp dụng bộ chia tỷ lệ cho dữ liệu trong X
    X_scaled = scaler.fit_transform(X)
    
    """
    Dòng này khởi tạo mô hình phân cụm KMeans với 3 cụm (n_clusters=3). random_state=42 được đặt để có thể tái tạo,
    đảm bảo rằng các kết quả nhất quán trong các lần chạy khác nhau.
    """
    kmeans = KMeans(n_clusters=3, random_state=42)
    """
    Dòng này áp dụng thuật toán KMeans cho dữ liệu đã chia tỷ lệ X_scaled và gán từng điểm dữ liệu cho một trong các cụm.
    """
    clusters = kmeans.fit_predict(X_scaled)
    
    # Adding cluster information to the DataFrame
    # Dòng này thêm một cột mới có tên là Cluster vào DataFrame df gốc
    df['Cluster'] = clusters
    """
    Dòng này in ra tên của tất cả các cột trong DataFrame df,
    bao gồm cả cột Cluster mới được thêm vào
    """
    print("Column names for clustering:", df.columns)
    
    
    # Make sure the DataFrame has appropriate columns for plotting
    feature_cols = ['Feature1', 'Feature2']  # Replace with actual feature columns
    """
    Dòng này kiểm tra xem cả hai feature_cols đã chỉ định có trong DataFrame df không. 
    Hàm all() trả về True nếu tất cả các cột trong feature_cols đều tồn tại trong df.columns.
    """
    if all(col in df.columns for col in feature_cols):
        # Dòng này tạo một hình mới để vẽ với kích thước đã chỉ định là 10x6 inch
        plt.figure(figsize=(10, 6))
        # òng này tạo một biểu đồ phân tán bằng hàm scatterplot của Seaborn
        sns.scatterplot(data=df, x='Feature1', y='Feature2', hue='Cluster', palette='viridis')
        #  Dòng này thêm tiêu đề cho biểu đồ
        plt.title('Clustering Results')
        # Dòng này hiển thị biểu đồ trên màn hình.
        plt.show()
        """
        nếu các cột đối tượng được chỉ định (Feature1, Feature2) không có trong DataFrame df.
        print("Feature1 và Feature2 không khả dụng. Hãy chọn các cột thích hợp để vẽ biểu đồ.")
        """
    else:
        """
        Dòng này in ra thông báo cho người dùng biết rằng các cột đối tượng được chỉ định không khả dụng trong DataFrame. 
        Nó gợi ý chọn các cột thích hợp để vẽ biểu đồ.
        """
        print("Feature1 and Feature2 are not available. Choose appropriate columns for plotting.")

# Main function to run the entire workflow
# điều phối toàn bộ quy trinhf làm việc tưf tải dữ liệu đến đào tạo mô hình và đánh giá 
def main(file_path):
    # tải dữ liệu file data 
    df = load_data(file_path)
    # khám phá dữ liệu
    explore_data(df)
    
    # trước khi xử lý dữ liệu ta gọi hàm preprocess_data để dọn dẹp và chuẩn bị dữ liệu
    df, (X_train, X_test, y_train, y_test) = preprocess_data(df)
    
    # đào tạo mô hình và lưu các mô hình khác nhau. 
    performance_metrics = train_and_evaluate_models(X_train, X_test, y_train, y_test)
    
    best_model_name = max(performance_metrics, key=lambda k: performance_metrics[k]['R²'])
    print(f"The best model based on R² score is: {best_model_name}")
    # lưu mô hình tốt nhất
    best_model = joblib.load(f'{best_model_name.replace(" ", "_")}_model.pkl')
    # kiểm tra mô hình tốt nhất.
    test_best_model(X_test, y_test, best_model)
    
    # thực hiện phân cụm và trực quan hóa kết quả
    clustering_analysis(df)

if __name__ == "__main__":
    # thực hiện đặt đường dẫn tệp: xác định đường dẫn tệp do dữ liệu
    file_path = 'Cost_of_Living_Index_by_Country_2024.csv'
    # thực hiện gọi hàm man() để dẫn tệp và bắt đầu quá trình làm việc
    main(file_path)


"""
DISCUSS: 

Chất lượng dữ liệu:

1/ Dữ liệu bị thiếu: Việc điền các giá trị bị thiếu bằng các giá trị trung bình không phải lúc nào cũng là cách tiếp cận tốt nhất, đặc biệt là nếu sự thiếu hụt không phải là ngẫu nhiên. Có thể cân nhắc các phương pháp quy kết tinh vi hơn.

2/ Giá trị ngoại lệ: Việc loại bỏ các giá trị ngoại lệ dựa trên điểm Z có thể dẫn đến mất dữ liệu có khả năng quan trọng.

3/ Mục tiêu tổng hợp: Việc sử dụng biến mục tiêu tổng hợp hữu ích để trình diễn, nhưng trong các tình huống thực tế, việc lựa chọn biến mục tiêu phải có ý nghĩa và liên quan trực tiếp đến vấn đề kinh doanh.

4/ Lựa chọn tính năng: Không phải tất cả các tính năng đều có liên quan. Các kỹ thuật lựa chọn tính năng, chẳng hạn như hồi quy Lasso, Loại bỏ tính năng đệ quy (RFE) hoặc sử dụng mức độ quan trọng của tính năng từ các mô hình như Rừng ngẫu nhiên, có thể cải thiện hiệu suất của mô hình.

5/ Mã hóa biến danh mục: Mã hóa một lần được sử dụng ở đây, nhưng trong một số trường hợp, các kỹ thuật mã hóa tiên tiến hơn như mã hóa mục tiêu hoặc nhúng có thể cải thiện hiệu suất, đặc biệt là với các tính năng có số lượng lớn.

6/ Lựa chọn mô hình: Việc lựa chọn mô hình bị giới hạn ở một số mô hình hồi quy. Khám phá các mô hình khác như Gradient Boosting Machines (GBM), XGBoost hoặc thậm chí là mạng nơ-ron có thể mang lại hiệu suất tốt hơn.

7/ Điều chỉnh siêu tham số: RandomizedSearchCV được sử dụng ở đây để điều chỉnh siêu tham số rất hiệu quả, nhưng các kỹ thuật khác như GridSearchCV hoặc tối ưu hóa Bayesian có thể được khám phá để tìm ra các siêu tham số tốt hơn nữa.

8/ Phương pháp tổng hợp: Kết hợp các dự đoán của nhiều mô hình có thể cải thiện hiệu suất bằng cách tận dụng thế mạnh của từng mô hình.

9/ Chiến lược CV: Chiến lược xác thực chéo nên được lựa chọn cẩn thận dựa trên dữ liệu. 

10/ Khả năng mở rộng: Khi tập dữ liệu phát triển, một số mô hình có thể trở nên tốn kém về mặt tính toán. Có thể cần khám phá các mô hình có khả năng mở rộng hơn hoặc các giải pháp điện toán phân tán.

11/ Triển khai: Đối với triển khai, các cân nhắc xung quanh khả năng diễn giải mô hình, độ trễ và tích hợp với các hệ thống hiện có là rất quan trọng. Các công cụ như joblib hữu ích để lưu các mô hình, nhưng đảm bảo rằng môi trường triển khai hỗ trợ các mô hình này cũng quan trọng không kém.

12/ Số cụm: Việc lựa chọn n_clusters=3 trong KMeans là tùy ý. Nó có thể không phản ánh cấu trúc cơ bản thực sự của dữ liệu. Các kỹ thuật như phương pháp khuỷu tay hoặc phân tích hình bóng có thể giúp xác định số cụm tối ưu.

13/ Diễn giải cụm: Sau khi các cụm được hình thành, việc hiểu được từng cụm đại diện cho điều gì là điều quan trọng. Phân tích sâu hơn, chẳng hạn như lập hồ sơ cụm hoặc sử dụng các thuật toán cụm khác, có thể cung cấp thông tin chi tiết sâu hơn.

"""