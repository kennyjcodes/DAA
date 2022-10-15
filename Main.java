import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        int[] arr = {7, 2, 4, 8, 6, 9, 1, 3};
        int start = 0;
        int end = arr.length;
        System.out.println(Arrays.toString(arr));
        merge_sort(arr, start, end);
        System.out.println(Arrays.toString(arr));
    }

    public static void merge_sort(int[] array, int start, int end) {
        if (end - start == 1) {
            return;
        }
        int mid = start + (end - start) / 2;
        merge_sort(array, start, mid);
        merge_sort(array, mid, end);
        merge(array, start, mid, end);
    }

    private static void merge(int[] arr, int start, int mid, int end) {
        int[] temp = new int[end - start];
        int i = start;
        int j = mid;
        int k = 0;
        while ((i < mid) && (j < end)) {
            if (arr[i] <= arr[j]) {
                temp[k] = arr[i];
                i++;
            }
            else {
                temp[k] = arr[j];
                j++;
            }
            k++;
        }
        while (i < mid) {
            temp[k] = arr[i];
            i++;
            k++;
        }
        while (j < end) {
            temp[k] = arr[j];
            j++;
            k++;
        }
        for (int n = 0; n < temp.length; n++) {
            arr[start + n] = temp[n];
        }
    }
}
